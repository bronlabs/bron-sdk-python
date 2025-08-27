from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class create_address_book_record(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: str
    externalId: str
    memo: Optional[str]
    name: str
    networkId: str
