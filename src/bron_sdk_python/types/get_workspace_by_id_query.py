from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class GetWorkspaceByIdQuery(TypedDict, total=False):
    workspaceIds: Optional[List[str]]
    includeSettings: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
