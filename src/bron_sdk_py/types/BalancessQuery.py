from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BalancessQuery(TypedDict, total=False):
    accountIds: Optional[List[str]]
    balanceIds: Optional[List[str]]
    assetIds: Optional[List[str]]
    networkId: Optional[str]
    accountTypes: Optional[List[AccountType]]
    excludedAccountTypes: Optional[List[AccountType]]
    nonEmpty: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
