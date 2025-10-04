from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class IntentsParams(TypedDict, total=False):
    feeLevel: Optional[FeeLevel]
    intentId: str
