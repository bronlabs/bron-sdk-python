from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeRewardInfo(TypedDict, total=False):
    increaseOperableBalance: Optional[bool]
    poolIds: Optional[List[str]]
    rewardSource: Optional[RewardSource]
    rewardWithoutTransaction: Optional[bool]
    stakeId: Optional[str]
