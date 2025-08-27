from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class user(TypedDict, total=False):
    allowedIps: Optional[List[str]]
    createdAt: Optional[str]
    createdBy: Optional[str]
    lastSignInAt: Optional[str]
    userId: str
