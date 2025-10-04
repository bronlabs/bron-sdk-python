from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Balance(TypedDict, total=False):
    accountId: str
    accountType: AccountType
    assetId: str
    balanceId: str
    createdAt: Optional[str]
    networkId: Optional[str]
    symbol: Optional[str]
    totalBalance: Optional[str]
    updatedAt: Optional[str]
    workspaceId: str
