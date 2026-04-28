from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionExtra(TypedDict, total=False):
    approvers: Optional[TransactionApprovers]
    blockchainDetails: Optional[List[BlockchainTxDetails]]
    blockchainRequest: Optional[BlockchainRequest]
    confirmations: Optional[str]
    depositTransactionId: Optional[str]
    description: Optional[str]
    fromAccountId: Optional[str]
    fromAddress: Optional[str]
    fromWorkspaceIcon: Optional[str]
    fromWorkspaceName: Optional[str]
    fromWorkspaceTag: Optional[str]
    memo: Optional[str]
    signingRequestId: Optional[str]
    toAccountId: Optional[str]
    toAddress: Optional[str]
    toWorkspaceIcon: Optional[str]
    toWorkspaceName: Optional[str]
    toWorkspaceTag: Optional[str]
    withdrawTransactionId: Optional[str]
