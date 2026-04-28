from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class UserProfile(TypedDict, total=False):
    icon: Optional[str]
    name: Optional[str]
    userId: str
