from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class NFTAllowanceParams(TypedDict, total=False):
    amount: Optional[str]
    approvalForAll: Optional[bool]
    assetId: str
    feeLevel: Optional[FeeLevel]
    networkFees: Optional[RequestedNetworkFees]
    toAddress: Optional[str]
    tokenId: Optional[str]
