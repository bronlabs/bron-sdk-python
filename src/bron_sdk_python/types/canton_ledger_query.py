from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CantonLedgerQuery(TypedDict, total=False):
    accountId: str
    params: Any
    sessionTopic: str
