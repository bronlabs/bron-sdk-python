from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class signing_request(TypedDict, total=False):
    accountId: Optional[str]
    blockchainNonce: Optional[str]
    messagesForSigning: Optional[messages_for_signing]
    networkId: Optional[str]
    requestParameters: Optional[Dict[str, Any]]
    shouldBeBroadcasted: Optional[bool]
    signed: Optional[signed]
    signingData: Optional[blockchain_signing_request]
    signingRequestId: Optional[str]
    status: Optional[signing_request_status]
    transactionId: Optional[str]
    transactionType: Optional[transaction_type]
    workspaceId: Optional[str]
