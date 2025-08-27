from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class balance(TypedDict, total=False):
    accountId: str
    accountType: account_type
    assetId: str
    balanceId: str
    createdAt: Optional[str]
    networkId: Optional[str]
    symbol: Optional[str]
    totalBalance: Optional[str]
    updatedAt: Optional[str]
    workspaceId: str
