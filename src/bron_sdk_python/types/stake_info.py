from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakeInfo(TypedDict, total=False):
    bondingAmount: Optional[str]
    bondingEndAt: Optional[str]
    claimableRewardsAmount: Optional[str]
    originPool: Optional[Pool]
    readyToClaimStakeAt: Optional[str]
    readyToIncrement: Optional[bool]
    readyToRedelegate: Optional[bool]
    readyToUnstake: Optional[bool]
    readyToUnstakeAt: Optional[str]
    rewardsRequireClaim: Optional[bool]
    unbondingAmount: Optional[str]
    unbondingEndAt: Optional[str]
    warning: Optional[Warning]
