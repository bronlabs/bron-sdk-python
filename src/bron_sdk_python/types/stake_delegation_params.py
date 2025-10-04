from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeDelegationParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    poolId: Optional[str]
