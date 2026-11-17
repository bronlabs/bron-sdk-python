from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateAddressBookRecord(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: Optional[str]
    bankDetails: Optional[BankDetails]
    email: Optional[str]
    externalId: str
    imageId: Optional[str]
    isFavorite: Optional[bool]
    labels: Optional[List[str]]
    memo: Optional[str]
    name: str
    networkId: Optional[str]
    note: Optional[str]
    recordType: Optional[RecordType]
    tag: Optional[str]
