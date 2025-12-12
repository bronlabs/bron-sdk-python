from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetAssetByIdQuery(TypedDict, total=False):
    assetIds: Optional[List[str]]
    networkIds: Optional[List[str]]
    symbolIds: Optional[List[str]]
    contractAddress: Optional[str]
    contractIssuer: Optional[str]
    assetType: Optional[AssetType]
    limit: Optional[str]
    offset: Optional[str]
