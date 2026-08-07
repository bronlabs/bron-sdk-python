from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class RawTransactionParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: Optional[str]
    data: Optional[str]
    externalBroadcast: Optional[bool]
    feeLevel: Optional[FeeLevel]
    networkFees: Optional[RequestedNetworkFees]
    networkId: Optional[str]
    rawTransactions: Optional[List[str]]
    skipSimulation: Optional[bool]
    toAddress: Optional[str]
