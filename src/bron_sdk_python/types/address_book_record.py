from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AddressBookRecord(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: Optional[str]
    createdAt: str
    createdBy: Optional[str]
    externalId: str
    imageId: Optional[str]
    lastUsedAt: Optional[str]
    memo: Optional[str]
    name: str
    networkId: Optional[str]
    recordId: str
    recordType: RecordType
    status: RecordStatus
    tag: Optional[str]
    updatedAt: Optional[str]
    updatedBy: Optional[str]
    workspaceId: str
