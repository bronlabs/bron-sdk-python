from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_networks_query(TypedDict, total=False):
    networkIds: Optional[List[str]]
