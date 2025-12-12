from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Warning(TypedDict, total=False):
    code: Optional[str]
    message: str
