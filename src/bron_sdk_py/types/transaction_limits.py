from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class transaction_limits(TypedDict, total=False):
    limits: List[transaction_limit]
