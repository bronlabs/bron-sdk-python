from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetSymbolByIdQuery(TypedDict, total=False):
    symbolIds: Optional[List[str]]
    assetIds: Optional[List[str]]
    limit: Optional[str]
    offset: Optional[str]
