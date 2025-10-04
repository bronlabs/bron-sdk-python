from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AllowanceParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    toAddress: str
    unlimited: Optional[bool]
