from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetAddressBookRecordsQuery(TypedDict, total=False):
    recordIds: Optional[List[str]]
    networkIds: Optional[List[str]]
    addresses: Optional[List[str]]
    memo: Optional[str]
    tag: Optional[str]
    limit: Optional[str]
    offset: Optional[str]
    recordType: Optional[RecordType]
    recordTypes: Optional[List[RecordType]]
    statuses: Optional[List[RecordStatus]]
