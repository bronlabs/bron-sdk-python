from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class WithdrawalParams(TypedDict, total=False):
    amount: str
    assetId: Optional[str]
    feeLevel: Optional[FeeLevel]
    includeFee: Optional[bool]
    memo: Optional[str]
    networkFees: Optional[RequestedNetworkFees]
    networkId: Optional[str]
    symbol: Optional[str]
    toAccountId: Optional[str]
    toAddress: Optional[str]
    toAddressBookRecordId: Optional[str]
    toWorkspaceTag: Optional[str]
