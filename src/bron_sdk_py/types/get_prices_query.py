from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_prices_query(TypedDict, total=False):
    baseSymbolIds: Optional[List[str]]
