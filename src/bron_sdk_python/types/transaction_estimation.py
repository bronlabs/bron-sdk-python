from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionEstimation(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    createdAt: str
    estimationId: str
    eventType: EventType
    extra: Optional[EventExtra]
    networkId: Optional[str]
    symbol: Optional[str]
    transactionId: str
    usdAmount: Optional[str]
