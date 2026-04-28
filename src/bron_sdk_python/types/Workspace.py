from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Workspace(TypedDict, total=False):
    icon: Optional[str]
    name: str
    tag: str
    workspaceId: str
