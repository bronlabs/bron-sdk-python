from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BlockchainSigningRequest(TypedDict, total=False):
    assetId: Optional[str]
    networkId: Optional[str]
    publicKey: Optional[str]
    sponsored: Optional[bool]
    transactionType: Optional[TransactionType]
