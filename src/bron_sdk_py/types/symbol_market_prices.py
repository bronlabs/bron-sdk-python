from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class symbol_market_prices(TypedDict, total=False):
    prices: List[symbol_market_price]
