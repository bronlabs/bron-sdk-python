from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventExtra(TypedDict, total=False):
    allowance: Optional[List[EventAllowance]]
    in: Optional[List[EventInput]]
    out: Optional[List[EventOutput]]
    rewardInfo: Optional[RewardInfo]
    stakeInfo: Optional[List[StakeInfo]]
    transactionFailed: Optional[bool]
