from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateIntent(TypedDict, total=False):
    accountId: str
    fromAmount: Optional[str]
    fromAssetId: str
    intentId: str
    toAmount: Optional[str]
    toAssetId: str
