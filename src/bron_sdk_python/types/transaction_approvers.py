from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionApprovers(TypedDict, total=False):
    approvedBy: Optional[List[str]]
    availableApprovers: Optional[List[str]]
    limitId: Optional[str]
    number: Optional[str]
    securityDelayDuration: Optional[str]
    securityDelayExpiresAt: Optional[str]
    skipApproval: Optional[bool]
