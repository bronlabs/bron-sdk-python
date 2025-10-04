from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetTransactionLimitsQuery(TypedDict, total=False):
    statuses: Optional[List[TransactionLimitStatus]]
    fromAccountIds: Optional[List[str]]
    toAddressBookRecordIds: Optional[List[str]]
    toAccountIds: Optional[List[str]]
    appliesToUserIds: Optional[List[str]]
    appliesToGroupIds: Optional[List[str]]
    limit: Optional[str]
    offset: Optional[str]
