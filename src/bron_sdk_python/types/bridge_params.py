from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BridgeParams(TypedDict, total=False):
    amount: str
    feeLevel: Optional[FeeLevel]
    sourceAssetId: str
