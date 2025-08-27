from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class workspace_member(TypedDict, total=False):
    _embedded: Optional[workspace_member_embedded]
    createdAt: str
    deactivatedAt: Optional[str]
    status: member_status
    updatedAt: Optional[str]
    userId: str
    workspaceId: str
