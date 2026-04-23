from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventExtra(TypedDict, total=False):
    allowance: Optional[List[EventAllowance]]
    in_: Optional[List[EventInput]]
    out: Optional[List[EventOutput]]
    rewardInfo: Optional[StakeRewardInfo]
    signingMessage: Optional[SigningMessage]
    stakeInfo: Optional[List[EventStakeInfo]]
    transactionFailed: Optional[bool]
