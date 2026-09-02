from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AccountExtra(TypedDict, total=False):
    onlyAddressBookWithdrawals: Optional[bool]
