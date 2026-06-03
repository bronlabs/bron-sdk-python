from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AssetPriceSeries(TypedDict, total=False):
    points: List[PriceSeriesPoint]
