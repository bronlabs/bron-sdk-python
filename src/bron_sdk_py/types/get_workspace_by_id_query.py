from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_workspace_by_id_query(TypedDict, total=False):
    workspaceIds: Optional[List[str]]
    includeSettings: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
