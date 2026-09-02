from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Pool(TypedDict, total=False):
    poolId: Optional[str]
    poolName: Optional[str]
    totalBonded: Optional[str]
