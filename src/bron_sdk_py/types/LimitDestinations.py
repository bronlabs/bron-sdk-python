from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitDestinations(TypedDict, total=False):
    accountIds: Optional[List[str]]
    addressBookRecordIds: Optional[List[str]]
    toAccounts: Optional[bool]
    toAddressBook: Optional[bool]
    toExternalAddresses: Optional[bool]
