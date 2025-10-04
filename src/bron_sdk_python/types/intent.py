from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Intent(TypedDict, total=False):
    createdAt: str
    expiresAt: Optional[str]
    fromAmount: Optional[str]
    fromAssetId: str
    intentId: str
    price: Optional[str]
    status: IntentOrderStatus
    toAmount: Optional[str]
    toAssetId: str
    updatedAt: str
    userSettlementDeadline: Optional[str]
