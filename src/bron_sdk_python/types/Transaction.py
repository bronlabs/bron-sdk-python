from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Transaction(TypedDict, total=False):
    accountId: str
    accountType: AccountType
    createdAt: str
    createdBy: Optional[str]
    embedded: Optional[TransactionEmbedded]
    expiresAt: Optional[str]
    externalId: str
    extra: Optional[TransactionExtra]
    params: Any
    status: TransactionStatus
    terminatedAt: Optional[str]
    transactionId: str
    transactionType: TransactionType
    updatedAt: Optional[str]
    workspaceId: str
