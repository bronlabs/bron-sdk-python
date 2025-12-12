from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class DryRunTransaction(TypedDict, total=False):
    accountId: str
    estimations: Optional[List[TransactionEstimation]]
    externalId: Optional[str]
    extra: Optional[TransactionExtra]
    params: Optional[Dict[str, Any]]
    transactionType: TransactionType
    warning: Optional[Warning]
