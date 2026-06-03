from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetAssetPriceSeriesQuery(TypedDict, total=False):
    baseSymbolId: Optional[str]
    period: Optional[ChartPeriod]
