from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_accounts_query(TypedDict, total=False):
    accountTypes: Optional[List[account_type]]
    excludedAccountTypes: Optional[List[account_type]]
    statuses: Optional[List[account_status]]
    accountIds: Optional[List[str]]
    isDefiVault: Optional[bool]
    offset: Optional[str]
    limit: Optional[str]
    isTestnet: Optional[bool]
