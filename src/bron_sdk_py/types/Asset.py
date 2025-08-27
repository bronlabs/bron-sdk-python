from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class asset(TypedDict, total=False):
    assetId: str
    assetType: Optional[asset_type]
    contractInformation: Optional[smart_contract_information]
    decimals: Optional[str]
    networkId: Optional[str]
    symbolId: Optional[str]
    verified: Optional[bool]
