from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Stakes(TypedDict, total=False):
    _embedded: Optional[StakesEmbedded]
    stakes: Optional[List[Stake]]
