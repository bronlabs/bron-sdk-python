from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BlockchainTxDetails(TypedDict, total=False):
    blockchainTxId: Optional[str]
    networkId: Optional[str]
