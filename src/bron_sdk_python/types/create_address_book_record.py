from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateAddressBookRecord(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: Optional[str]
    externalId: str
    imageId: Optional[str]
    memo: Optional[str]
    name: str
    networkId: Optional[str]
    recordType: Optional[RecordType]
    tag: Optional[str]
