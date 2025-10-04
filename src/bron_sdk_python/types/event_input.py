from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventInput(TypedDict, total=False):
    address: Optional[str]
    amount: Optional[str]
    fromAccountId: Optional[str]
    fromAddressBookRecordId: Optional[str]
    networkId: Optional[str]
