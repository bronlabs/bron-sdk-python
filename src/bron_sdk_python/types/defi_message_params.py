from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class DefiMessageParams(TypedDict, total=False):
    message: str
    networkId: str
    origin: str
    version: Optional[str]
