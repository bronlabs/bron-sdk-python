from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_deposit_addresses_query(TypedDict, total=False):
    accountId: Optional[str]
    addressIds: Optional[List[str]]
    externalId: Optional[str]
    accountTypes: Optional[List[account_type]]
    networkId: Optional[str]
    address: Optional[str]
    statuses: Optional[List[address_status]]
    sortDirection: Optional[sorting_direction]
    limit: Optional[str]
    offset: Optional[str]
