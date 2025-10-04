from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Assets(TypedDict, total=False):
    assets: Optional[List[Asset]]
