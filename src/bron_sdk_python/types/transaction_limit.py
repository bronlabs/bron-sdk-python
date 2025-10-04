from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionLimit(TypedDict, total=False):
    appliesTo: LimitAppliesTo
    createdAt: str
    createdBy: Optional[str]
    destinations: LimitDestinations
    externalId: str
    limitId: str
    limitRule: LimitRule
    limitType: TransactionLimitType
    sources: LimitSources
    status: TransactionLimitStatus
    transactionParams: LimitTransactionParams
    updatedAt: Optional[str]
    updatedBy: Optional[str]
    workspaceId: str
