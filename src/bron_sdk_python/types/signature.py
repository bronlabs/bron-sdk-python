from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Signature(TypedDict, total=False):
    e: Optional[str]
    r: Optional[str]
    rx: Optional[str]
    s: Optional[str]
    signature: Optional[str]
    v: Optional[str]
