from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_balances_query(TypedDict, total=False):
    accountIds: Optional[List[str]]
    balanceIds: Optional[List[str]]
    assetIds: Optional[List[str]]
    networkId: Optional[str]
    accountTypes: Optional[List[account_type]]
    excludedAccountTypes: Optional[List[account_type]]
    nonEmpty: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
