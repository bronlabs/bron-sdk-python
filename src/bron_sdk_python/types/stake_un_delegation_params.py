from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeUnDelegationParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    stakeId: Optional[str]
