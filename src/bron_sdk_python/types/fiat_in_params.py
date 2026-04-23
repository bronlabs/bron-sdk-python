from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatInParams(TypedDict, total=False):
    amount: str
    assetId: str
    fiatAmount: Optional[str]
    fiatAssetId: str
