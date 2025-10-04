from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeClaimParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    stakeId: Optional[str]
