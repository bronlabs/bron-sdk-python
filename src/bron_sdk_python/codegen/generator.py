from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class OpenApiSchema:
    type: Optional[str] = None
    enum: Optional[List[Any]] = None
    ref: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    additionalProperties: Optional[Any] = None
    required: Optional[List[str]] = None
    items: Optional[Dict[str, Any]] = None
    allOf: Optional[List[Dict[str, Any]]] = None
    oneOf: Optional[List[Dict[str, Any]]] = None
    anyOf: Optional[List[Dict[str, Any]]] = None


class OpenApiSdkGenerator:
    def __init__(self, spec_path: str, types_dir: str, api_dir: str) -> None:
        self.spec = self._load_spec(spec_path)
        self.types_dir = types_dir
        self.api_dir = api_dir

    def generate(self) -> None:
        self._prepare_dir(self.types_dir, ".py")
        self._prepare_dir(self.api_dir, ".py")

        self._generate_types()
        self._generate_api()

    def _load_spec(self, spec_path: str) -> Dict[str, Any]:
        with open(spec_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _prepare_dir(self, directory: str, extension: str) -> None:
        os.makedirs(directory, exist_ok=True)
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path) and name.endswith(extension) and name != "__init__.py":
                os.remove(path)

    # ---------- Types ----------
    def _generate_types(self) -> None:
        schemas: Dict[str, Any] = self.spec.get("components", {}).get("schemas", {})
        for name, schema in schemas.items():
            content, module_name = self._generate_type_definition(name, schema)
            with open(os.path.join(self.types_dir, f"{module_name}.py"), "w", encoding="utf-8") as f:
                f.write(content + "\n")

    def _generate_type_definition(self, name: str, schema: Dict[str, Any]) -> Tuple[str, str]:
        class_name = self._to_pascal(name)
        module_name = self._to_snake(name)

        if schema.get("enum"):
            return self._generate_enum(class_name, schema), module_name

        if schema.get("allOf") and len(schema["allOf"]) == 1 and schema["allOf"][0].get("$ref"):
            ref_class, ref_module = self._extract_ref_class_module(schema["allOf"][0]["$ref"])
            return f"from .{ref_module} import {ref_class} as {class_name}", module_name

        if schema.get("$ref"):
            ref_class, ref_module = self._extract_ref_class_module(schema["$ref"])
            return f"from .{ref_module} import {ref_class} as {class_name}", module_name

        if self._is_empty_object(schema):
            return f"from typing import Dict, Any\n\n{class_name} = Dict[str, Any]", module_name

        if schema.get("type") == "object" or schema.get("properties"):
            return self._generate_typed_dict(class_name, schema), module_name

        return f"from typing import Any\n\n{class_name} = Any", module_name

    def _generate_enum(self, class_name: str, schema: Dict[str, Any]) -> str:
        lines = ["from enum import Enum", "\n", f"class {class_name}(Enum):"]
        for v in schema.get("enum", []):
            if isinstance(v, str):
                const_name = re.sub(r"[^A-Za-z0-9_]", "_", v.upper())
                if const_name and const_name[0].isdigit():
                    const_name = "TYPE_" + const_name
                lines.append(f"    {const_name} = \"{v}\"")
        return "\n".join(lines)

    def _generate_typed_dict(self, class_name: str, schema: Dict[str, Any]) -> str:
        import keyword
    
        required = set(schema.get("required", []) or [])
        props = schema.get("properties", {}) or {}
        imports: List[str] = [
            "from __future__ import annotations",
            "from typing import Any, Dict, List, Optional, TypedDict",
        ]

        fields: List[str] = []
        for prop, prop_schema in props.items():
            safe_name = prop + "_" if keyword.iskeyword(prop) else prop
            py_type = self._resolve_type(prop_schema)
            final_type = py_type if prop in required else ("Optional[{}]".format(py_type) if py_type != "Any" else "Any")
            fields.append(f"    {safe_name}: {final_type}")

        return "\n".join(imports + ["", f"class {class_name}(TypedDict, total=False):"] + (fields or ["    pass"]))

    def _resolve_type(self, schema: Dict[str, Any]) -> str:
        if "$ref" in schema:
            ref_class, _ = self._extract_ref_class_module(schema["$ref"])
            return ref_class
        t = schema.get("type")
        if schema.get("enum"):
            return "str"
        if t == "string":
            return "str"
        if t == "integer":
            return "int"
        if t == "number":
            return "float"
        if t == "boolean":
            return "bool"
        if t == "array":
            items = schema.get("items") or {}
            return f"List[{self._resolve_type(items)}]"
        if t == "object":
            return "Dict[str, Any]"
        return "Any"

    def _is_empty_object(self, schema: Dict[str, Any]) -> bool:
        has_obj = schema.get("type") == "object" or bool(schema.get("properties") or schema.get("additionalProperties"))
        no_props = not schema.get("properties")
        addl = schema.get("additionalProperties")
        is_free = addl is None or addl is True
        return has_obj and no_props and is_free

    # ---------- API ----------
    def _generate_api(self) -> None:
        paths = self.spec.get("paths", {})
        file_data: Dict[str, Dict[str, Any]] = {}

        for route, methods in paths.items():
            for method, op in methods.items():
                summary = op.get("summary")
                if not summary:
                    continue
                file_name = self._get_file_name(op)
                file_data.setdefault(file_name, {"types": set(), "methods": []})

                return_type = self._get_return_type(op)
                if return_type:
                    file_data[file_name]["types"].add(return_type)

                body_type = self._get_request_body_type(op)
                if body_type:
                    file_data[file_name]["types"].add(body_type)

                method_code, qtype_class = self._generate_method(op, method, route)
                if qtype_class:
                    file_data[file_name]["types"].add(qtype_class)
                file_data[file_name]["methods"].append(method_code)

        for file_name, data in file_data.items():
            content = self._generate_api_file(file_name, data)
            with open(os.path.join(self.api_dir, f"{file_name}.py"), "w", encoding="utf-8") as f:
                f.write(content)

    def _generate_api_file(self, file_name: str, data: Dict[str, Any]) -> str:
        class_name = f"{file_name[0].upper()}{file_name[1:]}API"
        imports = [
            "from __future__ import annotations",
            "from typing import Optional, TYPE_CHECKING, cast",
            "from ..utils.http import HttpClient",
        ]
        type_imports: List[str] = []
        used_types = sorted(list(data.get("types", set())))

        if used_types:
            type_imports.append("if TYPE_CHECKING:")
            for t in used_types:
                mod = self._to_snake(t)
                type_imports.append(f"    from ..types.{mod} import {t}")

        return "\n".join(
            imports + type_imports + [
                "",
                f"class {class_name}:",
                "    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:",
                "        self._http = http",
                "        self._workspace_id = workspace_id",
                "",
                *data["methods"],
                "",
            ]
        )

    def _generate_method(self, op: Dict[str, Any], method: str, route: str) -> Tuple[str, Optional[str]]:
        func_name = self._to_snake(op.get("summary", "").replace("ID", "Id"))

        path_params = [p for p in op.get("parameters", []) if p.get("in") == "path" and p.get("name") != "workspaceId"]
        query_params = [p for p in op.get("parameters", []) if p.get("in") == "query"]
        has_body = bool(op.get("requestBody", {}).get("content", {}).get("application/json"))

        args: List[str] = ["self"]
        for p in path_params:
            args.append(f"{p['name']}: str")

        qtype_class: Optional[str] = None
        if query_params:
            method_pascal = self._to_pascal(op.get("summary", "").replace("ID", "Id"))
            qtype_class = f"{method_pascal}Query"
            qp: Dict[str, Any] = {}
            for p in query_params:
                pname = p.get("name")
                if pname and pname != "workspaceId":
                    qp[pname] = p.get("schema") or {}
            self._write_query_type_file(qtype_class, qp)
            args.append(f"query: Optional[{qtype_class}] = None")

        if has_body:
            body_type = self._get_request_body_type(op)
            if body_type:
                args.append(f"body: Optional[{body_type}] = None")
            else:
                args.append("body: Optional[dict] = None")

        path_expr = route.replace("{workspaceId}", "{ws}")
        for p in path_params:
            path_expr = path_expr.replace("{" + p["name"] + "}", "{" + p["name"] + "}")

        path_build = [f"path = \"{path_expr}\""]
        if "{ws}" in path_expr:
            path_build.append("path = path.format(ws=self._workspace_id, **locals())")
        else:
            path_build.append("path = path.format(**locals())")

        call_args = [f"method='{method.upper()}'", "path=path"]
        if qtype_class:
            call_args.append("query=query")
        if has_body:
            call_args.append("body=body")

        return_type = self._get_return_type(op)
        ret_annot = f" -> \"{return_type}\"" if return_type else ""

        call_expr = f"await self._http.request({', '.join(call_args)})"
        if return_type:
            call_expr = f"cast(\"{return_type}\", {call_expr})"

        method_src = "\n".join(
            [
                f"    async def {func_name}({', '.join(args)}){ret_annot}:",
                f"        {path_build[0]}",
                f"        {path_build[1]}",
                f"        return {call_expr}",
                "",
            ]
        )
        return method_src, qtype_class

    def _write_query_type_file(self, class_name: str, params: Dict[str, Any]) -> None:
        module_name = self._to_snake(class_name)
        imports = [
            "from __future__ import annotations",
            "from typing import Any, Dict, List, Optional, TypedDict",
        ]
        fields: List[str] = []
        for pname, pschema in (params or {}).items():
            py_type = self._resolve_type(pschema or {})
            opt_type = f"Optional[{py_type}]" if py_type != "Any" else "Any"
            fields.append(f"    {pname}: {opt_type}")
        content = "\n".join(imports + ["", f"class {class_name}(TypedDict, total=False):"] + (fields or ["    pass"]))
        with open(os.path.join(self.types_dir, f"{module_name}.py"), "w", encoding="utf-8") as f:
            f.write(content + "\n")

    def _get_request_body_type(self, op: Dict[str, Any]) -> Optional[str]:
        body = (op.get("requestBody") or {}).get("content", {}).get("application/json", {})
        schema = body.get("schema") if isinstance(body, dict) else None
        if schema and schema.get("$ref"):
            ref_class, _ = self._extract_ref_class_module(schema["$ref"])
            return ref_class
        return None

    def _get_return_type(self, op: Dict[str, Any]) -> Optional[str]:
        for code in ("200", "201"):
            resp = op.get("responses", {}).get(code)
            if not resp:
                continue
            schema = resp.get("content", {}).get("application/json", {}).get("schema")
            if schema and schema.get("$ref"):
                ref_class, _ = self._extract_ref_class_module(schema["$ref"])
                return ref_class
        return None

    def _get_file_name(self, op: Dict[str, Any]) -> str:
        tags = op.get("tags") or []
        return self._to_camel(tags[0]) if tags else "misc"

    def _extract_ref_class_module(self, ref: str) -> Tuple[str, str]:
        last = ref.split("/")[-1]
        return self._to_pascal(last), self._to_snake(last)

    def _to_camel(self, s: str) -> str:
        if not s:
            return s
        if re.search(r"[A-Z]", s) and not re.search(r"[-_ ]", s):
            return s[0].lower() + s[1:]
        parts = re.split(r"[-_ ]+", s)
        return parts[0].lower() + "".join(p.capitalize() for p in parts[1:])

    def _to_pascal(self, s: str) -> str:
        return re.sub(r"(^|[^a-zA-Z0-9]+)([a-zA-Z0-9])", lambda m: (m.group(2) or "").upper(), s)

    def _to_snake(self, s: str) -> str:
        if not s:
            return s
        s = re.sub(r"[\-\s]+", "_", s)
        s = re.sub(r"([^_])([A-Z][a-z]+)", r"\1_\2", s)
        s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
        s = s.replace("__", "_")
        return s.lower()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("spec_file")
    parser.add_argument("types_dir")
    parser.add_argument("api_dir")
    args = parser.parse_args()

    gen = OpenApiSdkGenerator(args.spec_file, args.types_dir, args.api_dir)
    gen.generate()


if __name__ == "__main__":
    main()
