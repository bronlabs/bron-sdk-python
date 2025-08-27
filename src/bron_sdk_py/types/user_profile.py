from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class user_profile(TypedDict, total=False):
    imageId: Optional[str]
    name: Optional[str]
    userId: str
