from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionEvent(TypedDict, total=False):
    accountId: str
    accountType: AccountType
    amount: Optional[str]
    assetId: str
    blockchainTxId: Optional[str]
    createdAt: str
    eventId: str
    eventType: EventType
    extra: Optional[EventExtra]
    networkId: Optional[str]
    symbol: Optional[str]
    transactionId: str
    usdAmount: Optional[str]
    workspaceId: str
