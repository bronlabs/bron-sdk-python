from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Transactions(TypedDict, total=False):
    _embedded: Optional[TransactionEmbedded]
    transactions: List[Transaction]
