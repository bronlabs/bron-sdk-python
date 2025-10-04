from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetPricesQuery(TypedDict, total=False):
    baseSymbolIds: Optional[List[str]]
