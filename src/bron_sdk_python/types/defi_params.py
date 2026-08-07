from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class DefiParams(TypedDict, total=False):
    data: Optional[str]
    externalBroadcast: Optional[bool]
    feeLevel: Optional[FeeLevel]
    method: str
    networkId: str
    origin: str
    rawTransaction: Optional[str]
    rawTransactions: Optional[List[str]]
    to: Optional[str]
    value: Optional[str]
