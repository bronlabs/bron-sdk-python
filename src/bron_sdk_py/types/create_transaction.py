from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class create_transaction(TypedDict, total=False):
    accountId: str
    expiresAt: Optional[str]
    externalId: str
    params: Any
    transactionType: transaction_type
