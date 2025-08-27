from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class transaction_extra(TypedDict, total=False):
    approvers: Optional[transaction_approvers]
    blockchainDetails: Optional[List[blockchain_tx_details]]
    blockchainRequest: Optional[blockchain_request]
    confirmations: Optional[str]
    depositTransactionId: Optional[str]
    description: Optional[str]
    externalBroadcast: Optional[bool]
    fromAccountId: Optional[str]
    fromAddress: Optional[str]
    memo: Optional[str]
    signingRequestId: Optional[str]
    toAccountId: Optional[str]
    toAddress: Optional[str]
    withdrawTransactionId: Optional[str]
