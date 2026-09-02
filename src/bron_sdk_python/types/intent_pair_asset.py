from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class IntentPairAsset(TypedDict, total=False):
    assetId: str
    contractAddress: Optional[str]
    decimals: str
    name: Optional[str]
    networkId: str
    symbol: str
