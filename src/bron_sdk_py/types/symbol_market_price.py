from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class symbol_market_price(TypedDict, total=False):
    baseSymbolId: str
    price: str
    quoteSymbolId: str
