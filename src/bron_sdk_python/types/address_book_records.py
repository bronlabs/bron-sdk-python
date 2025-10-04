from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AddressBookRecords(TypedDict, total=False):
    records: List[AddressBookRecord]
