from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateTransaction(TypedDict, total=False):
    accountId: str
    description: Optional[str]
    expiresAt: Optional[str]
    externalId: str
    params: Any
    transactionType: TransactionType
