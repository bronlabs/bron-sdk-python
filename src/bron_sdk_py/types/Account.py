from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Account(TypedDict, total=False):
    accountId: str
    accountName: str
    accountType: AccountType
    createdAt: str
    createdBy: Optional[str]
    externalId: str
    extra: Optional[AccountExtra]
    isTestnet: Optional[bool]
    parentAccountId: Optional[str]
    status: AccountStatus
    updatedAt: Optional[str]
    workspaceId: str
