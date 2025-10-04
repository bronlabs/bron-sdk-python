from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AddressBookRecord(TypedDict, total=False):
    accountIds: Optional[List[str]]
    address: str
    createdAt: str
    createdBy: Optional[str]
    externalId: str
    lastUsedAt: Optional[str]
    memo: Optional[str]
    name: str
    networkId: str
    recordId: str
    status: RecordStatus
    updatedAt: Optional[str]
    updatedBy: Optional[str]
    workspaceId: str
