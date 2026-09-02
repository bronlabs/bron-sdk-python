from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class StakesEmbedded(TypedDict, total=False):
    resourceRentalRewardsAmounts: Optional[List[RewardsAmount]]
    rewardsAmounts: Optional[List[RewardsAmount]]
