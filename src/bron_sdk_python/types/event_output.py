from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventOutput(TypedDict, total=False):
    address: Optional[str]
    amount: Optional[str]
    memo: Optional[str]
    networkId: Optional[str]
    toAccountId: Optional[str]
    toAddressBookRecordId: Optional[str]
