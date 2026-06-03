from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class RequestIndicativeSwapQuoteQuery(TypedDict, total=False):
    fromAssetId: Optional[str]
    toAssetId: Optional[str]
    fromAmount: Optional[str]
    toAmount: Optional[str]
