from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitAppliesTo(TypedDict, total=False):
    userIds: Optional[List[str]]
