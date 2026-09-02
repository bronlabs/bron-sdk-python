from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventStakeInfo(TypedDict, total=False):
    amount: Optional[str]
    poolId: Optional[str]
    resource: Optional[str]
    stakeId: Optional[str]
