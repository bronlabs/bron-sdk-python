from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitRuleApprove(TypedDict, total=False):
    authorisedApproversUserIds: Optional[List[str]]
    numberOfApprovals: str
