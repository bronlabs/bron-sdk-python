from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class CreateTransactions(TypedDict, total=False):
    transactions: List[CreateTransaction]
