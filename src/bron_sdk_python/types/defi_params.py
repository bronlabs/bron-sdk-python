from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class DefiParams(TypedDict, total=False):
    data: Optional[str]
    externalBroadcast: Optional[bool]
    feeLevel: Optional[FeeLevel]
    networkId: str
    origin: str
    rawTransactions: Optional[List[str]]
    to: Optional[str]
    value: Optional[str]
