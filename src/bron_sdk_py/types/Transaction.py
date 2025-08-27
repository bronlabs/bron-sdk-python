from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class transaction(TypedDict, total=False):
    accountId: str
    accountType: account_type
    createdAt: str
    createdBy: Optional[str]
    embedded: Optional[transaction_embedded]
    expiresAt: Optional[str]
    externalId: str
    extra: Optional[transaction_extra]
    params: Any
    status: transaction_status
    terminatedAt: Optional[str]
    transactionId: str
    transactionType: transaction_type
    updatedAt: Optional[str]
    workspaceId: str
