from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetAssetsQuery(TypedDict, total=False):
    assetIds: Optional[List[str]]
    networkIds: Optional[List[str]]
    symbolIds: Optional[List[str]]
    contractAddress: Optional[str]
    contractIssuer: Optional[str]
    assetType: Optional[AssetType]
    search: Optional[str]
    limit: Optional[str]
    offset: Optional[str]
