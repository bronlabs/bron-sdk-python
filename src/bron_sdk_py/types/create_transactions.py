from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class create_transactions(TypedDict, total=False):
    transactions: List[create_transaction]
