import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pyproject = ROOT / "pyproject.toml"
version_file = ROOT / "src/bron_sdk_python/utils/version.py"

content = pyproject.read_text(encoding="utf-8")
match = re.search(r"^version\s*=\s*\"([^\"]+)\"", content, flags=re.M)
if not match:
    raise SystemExit("Could not find version in pyproject.toml")
version = match.group(1)

version_py = f'SDK_VERSION = "{version}"'

version_file.write_text(version_py, encoding="utf-8")
print(f"Updated SDK_VERSION to {version}")
