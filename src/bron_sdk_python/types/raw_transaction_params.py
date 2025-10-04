from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class RawTransactionParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    data: Optional[str]
    feeLevel: Optional[FeeLevel]
    rawTransactions: Optional[List[str]]
    toAddress: str
