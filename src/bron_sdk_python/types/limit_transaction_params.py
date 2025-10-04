from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitTransactionParams(TypedDict, total=False):
    aboveAmount: Optional[LimitAmount]
    durationHours: Optional[str]
