from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class withdrawal_params(TypedDict, total=False):
    amount: str
    assetId: Optional[str]
    feeLevel: Optional[fee_level]
    includeFee: Optional[bool]
    memo: Optional[str]
    networkFees: Optional[requested_network_fees]
    networkId: Optional[str]
    symbol: Optional[str]
    toAccountId: Optional[str]
    toAddress: Optional[str]
    toAddressBookRecordId: Optional[str]
