from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitSources(TypedDict, total=False):
    accountIds: Optional[List[str]]
