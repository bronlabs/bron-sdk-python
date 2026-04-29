from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AssetMarketPrice(TypedDict, total=False):
    baseAssetId: str
    baseSymbolId: str
    price: str
    quoteAssetId: str
    quoteSymbolId: str
