from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class account(TypedDict, total=False):
    accountId: str
    accountName: str
    accountType: account_type
    createdAt: str
    createdBy: Optional[str]
    externalId: str
    extra: Optional[account_extra]
    isTestnet: Optional[bool]
    parentAccountId: Optional[str]
    status: account_status
    updatedAt: Optional[str]
    workspaceId: str
