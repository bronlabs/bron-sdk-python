from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class NFTWithdrawalParams(TypedDict, total=False):
    amount: str
    assetId: str
    feeLevel: Optional[FeeLevel]
    includeFee: Optional[bool]
    networkFees: Optional[RequestedNetworkFees]
    toAccountId: Optional[str]
    toAddress: Optional[str]
    toAddressBookRecordId: Optional[str]
    tokenId: str
