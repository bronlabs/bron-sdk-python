from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Network(TypedDict, total=False):
    addressExplorerUrl: Optional[str]
    confirmations: Optional[str]
    explorerUrl: Optional[str]
    isTestnet: Optional[bool]
    name: Optional[str]
    nativeAssetId: Optional[str]
    nativeAssetSymbol: Optional[str]
    networkId: Optional[str]
    tags: Optional[List[NetworkTag]]
