from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetBalancesQuery(TypedDict, total=False):
    accountId: Optional[str]
    accountIds: Optional[List[str]]
    balanceIds: Optional[List[str]]
    assetId: Optional[str]
    assetIds: Optional[List[str]]
    assetNotIn: Optional[List[str]]
    networkId: Optional[str]
    networkIds: Optional[List[str]]
    accountTypes: Optional[List[AccountType]]
    excludedAccountTypes: Optional[List[AccountType]]
    updatedSince: Optional[str]
    nonEmpty: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
