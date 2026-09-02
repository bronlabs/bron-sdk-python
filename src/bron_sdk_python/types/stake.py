from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Stake(TypedDict, total=False):
    accountId: Optional[str]
    amount: Optional[str]
    assetId: Optional[str]
    networkId: Optional[str]
    poolId: Optional[str]
    stakeId: Optional[str]
    stakeInfo: Optional[StakeInfo]
    status: Optional[StakeStatus]
    updatedAt: Optional[str]
    warning: Optional[Warning]
    workspaceId: Optional[str]
