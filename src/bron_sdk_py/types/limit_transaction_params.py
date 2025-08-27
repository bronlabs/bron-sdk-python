from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class limit_transaction_params(TypedDict, total=False):
    aboveAmount: Optional[limit_amount]
    durationHours: Optional[str]
