from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BronLockBurnExtra(TypedDict, total=False):
    redeemRequestId: Optional[str]
    releaseBlockchainTxId: Optional[str]
    releaseSigningRequestId: Optional[str]
    releaseTransactionId: Optional[str]
