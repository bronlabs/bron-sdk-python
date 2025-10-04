from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetDepositAddressesQuery(TypedDict, total=False):
    accountId: Optional[str]
    addressIds: Optional[List[str]]
    externalId: Optional[str]
    accountTypes: Optional[List[AccountType]]
    networkId: Optional[str]
    address: Optional[str]
    statuses: Optional[List[AddressStatus]]
    sortDirection: Optional[SortingDirection]
    limit: Optional[str]
    offset: Optional[str]
