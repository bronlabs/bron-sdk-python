from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class transaction_limit(TypedDict, total=False):
    appliesTo: limit_applies_to
    createdAt: str
    createdBy: Optional[str]
    destinations: limit_destinations
    externalId: str
    limitId: str
    limitRule: limit_rule
    limitType: transaction_limit_type
    sources: limit_sources
    status: transaction_limit_status
    transactionParams: limit_transaction_params
    updatedAt: Optional[str]
    updatedBy: Optional[str]
    workspaceId: str
