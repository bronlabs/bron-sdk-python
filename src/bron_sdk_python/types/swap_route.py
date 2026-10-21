from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SwapRoute(TypedDict, total=False):
    accountId: str
    externalId: Optional[str]
    fromAmount: Optional[str]
    fromAssetId: str
    fromTokenId: Optional[str]
    toAmount: Optional[str]
    toAssetId: str
    toTokenId: Optional[str]
