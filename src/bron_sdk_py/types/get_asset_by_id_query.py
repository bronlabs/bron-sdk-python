from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_asset_by_id_query(TypedDict, total=False):
    assetIds: Optional[List[str]]
    networkIds: Optional[List[str]]
    symbolIds: Optional[List[str]]
    contractAddress: Optional[str]
    assetType: Optional[asset_type]
    limit: Optional[str]
    offset: Optional[str]
