from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class IntentsQuote(TypedDict, total=False):
    _embedded: Optional[IntentsQuoteEmbedded]
    fromAmount: str
    fromAssetId: str
    minPrice: str
    minToAmount: str
    oracleFeePercent: str
    solverFeePercent: str
    toAmount: str
    toAssetId: str
