from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeWithdrawalParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    poolId: Optional[str]
