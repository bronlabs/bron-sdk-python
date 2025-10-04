from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SymbolMarketPrices(TypedDict, total=False):
    prices: List[SymbolMarketPrice]
