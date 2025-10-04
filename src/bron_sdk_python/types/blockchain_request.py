from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BlockchainRequest(TypedDict, total=False):
    externalBroadcast: Optional[bool]
    networkId: Optional[str]
