from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SigningRequest(TypedDict, total=False):
    accountId: Optional[str]
    blockchainNonce: Optional[str]
    messagesForSigning: Optional[MessagesForSigning]
    networkId: Optional[str]
    requestParameters: Optional[Dict[str, Any]]
    shouldBeBroadcasted: Optional[bool]
    signed: Optional[Signed]
    signingData: Optional[BlockchainSigningRequest]
    signingRequestId: Optional[str]
    status: Optional[SigningRequestStatus]
    transactionId: Optional[str]
    transactionType: Optional[TransactionType]
    workspaceId: Optional[str]
