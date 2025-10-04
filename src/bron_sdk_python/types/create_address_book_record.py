from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateAddressBookRecord(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: str
    externalId: str
    memo: Optional[str]
    name: str
    networkId: str
