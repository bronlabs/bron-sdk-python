from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class DepositParams(TypedDict, total=False):
    amount: str
    assetId: str
    networkId: str
