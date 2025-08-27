from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_stakes_query(TypedDict, total=False):
    accountId: Optional[str]
    assetId: Optional[str]
    rewardPeriod: Optional[str]
