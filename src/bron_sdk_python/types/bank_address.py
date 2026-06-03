from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BankAddress(TypedDict, total=False):
    address: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postalCode: Optional[str]
    state: Optional[str]
