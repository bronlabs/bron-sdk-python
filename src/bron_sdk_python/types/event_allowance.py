from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class EventAllowance(TypedDict, total=False):
    address: Optional[str]
    amount: Optional[str]
    networkId: Optional[str]
    unlimited: Optional[bool]
