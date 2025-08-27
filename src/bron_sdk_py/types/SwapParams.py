from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SwapParams(TypedDict, total=False):
    fromAmount: Optional[str]
    fromAssetId: str
    quoteId: str
    toAmount: Optional[str]
    toAssetId: str
