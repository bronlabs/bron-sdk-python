import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pyproject = ROOT / "pyproject.toml"
version_file = ROOT / "src/bron_sdk_python/utils/version.py"

version = os.environ.get("VERSION")
if not version:
    raise SystemExit("VERSION env variable is required")

content = pyproject.read_text(encoding="utf-8")
new_content, count = re.subn(
    r'(^version\s*=\s*")[^"]+(")',
    rf'\g<1>{version}\2',
    content,
    flags=re.M,
)
if count == 0:
    raise SystemExit("Could not find version in pyproject.toml")

pyproject.write_text(new_content, encoding="utf-8")
version_file.write_text(f'SDK_VERSION = "{version}"\n', encoding="utf-8")

print(f"Updated version to {version}")
