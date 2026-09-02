from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class PriceSeriesPoint(TypedDict, total=False):
    baseSymbolId: str
    close: str
    high: str
    low: str
    open: str
    timestamp: str
    volume24h: str
