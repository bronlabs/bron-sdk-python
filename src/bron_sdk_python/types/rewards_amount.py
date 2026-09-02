from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class RewardsAmount(TypedDict, total=False):
    amount: Optional[str]
    assetId: Optional[str]
