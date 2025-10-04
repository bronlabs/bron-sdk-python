from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetNetworksQuery(TypedDict, total=False):
    networkIds: Optional[List[str]]
