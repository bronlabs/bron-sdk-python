from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetAccountsQuery(TypedDict, total=False):
    accountTypes: Optional[List[AccountType]]
    excludedAccountTypes: Optional[List[AccountType]]
    statuses: Optional[List[AccountStatus]]
    accountIds: Optional[List[str]]
    isDefiVault: Optional[bool]
    offset: Optional[str]
    limit: Optional[str]
    isTestnet: Optional[bool]
