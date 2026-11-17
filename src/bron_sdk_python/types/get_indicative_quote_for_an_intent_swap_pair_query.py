from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetIndicativeQuoteForAnIntentSwapPairQuery(TypedDict, total=False):
    fromAmount: Optional[str]
    toAmount: Optional[str]
    broadcasterFeePercent: Optional[str]
