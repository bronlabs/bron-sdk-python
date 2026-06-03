from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CantonLedgerQueryResult(TypedDict, total=False):
    result: Any
    status: Optional[str]
