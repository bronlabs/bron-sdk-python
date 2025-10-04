from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Asset(TypedDict, total=False):
    assetId: str
    assetType: Optional[AssetType]
    contractInformation: Optional[SmartContractInformation]
    decimals: Optional[str]
    networkId: Optional[str]
    symbolId: Optional[str]
    verified: Optional[bool]
