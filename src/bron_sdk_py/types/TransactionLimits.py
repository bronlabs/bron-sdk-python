from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionLimits(TypedDict, total=False):
    limits: List[TransactionLimit]
