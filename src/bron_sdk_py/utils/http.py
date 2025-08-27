from __future__ import annotations

import json
from typing import Any, Dict, Optional

import httpx

from .auth import generate_bron_jwt, parse_jwk_ec_private_key
from .version import SDK_VERSION


class HttpClient:
    def __init__(self, base_url: str, api_key_jwk: str, *, timeout: Optional[float] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key_jwk = api_key_jwk
        self.user_agent = f"Bron SDK PY/{SDK_VERSION}"
        self._client = httpx.AsyncClient(timeout=timeout)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def request(self, *, method: str, path: str, body: Optional[dict] = None, query: Optional[dict] = None) -> Any:
        full_path = path
        if query:
            params = []
            for k, v in query.items():
                if v is None:
                    continue
                if isinstance(v, list):
                    params.append((k, ",".join(str(e) for e in v)))
                else:
                    params.append((k, str(v)))
            if params:
                from urllib.parse import urlencode

                full_path = f"{full_path}?{urlencode(params)}"

        url = f"{self.base_url}{full_path}"

        _, kid = parse_jwk_ec_private_key(self.api_key_jwk)
        body_str = json_dumps_no_nones(body) if body is not None else ""
        jwt_token = generate_bron_jwt(
            method=method,
            path=full_path,
            body=body_str,
            kid=kid,
            private_jwk=self.api_key_jwk,
        )

        headers: Dict[str, str] = {
            "Authorization": f"ApiKey {jwt_token}",
            "User-Agent": self.user_agent,
        }
        if body is not None:
            headers["Content-Type"] = "application/json"

        res = await self._client.request(method=method, url=url, headers=headers, content=body_str if body is not None else None)

        if res.status_code >= 400:
            raise RuntimeError(f"HTTP {res.status_code}: {res.text}")

        if res.content:
            return res.json()
        return None


def json_dumps_no_nones(obj: Any) -> str:
    def prune_none(o: Any) -> Any:
        if isinstance(o, dict):
            return {k: prune_none(v) for k, v in o.items() if v is not None}
        if isinstance(o, list):
            return [prune_none(v) for v in o]
        return o

    return json.dumps(prune_none(obj), separators=(",", ":"))


