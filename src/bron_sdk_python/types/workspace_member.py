from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class WorkspaceMember(TypedDict, total=False):
    _embedded: Optional[WorkspaceMemberEmbedded]
    createdAt: str
    deactivatedAt: Optional[str]
    status: MemberStatus
    updatedAt: Optional[str]
    userId: str
    workspaceId: str
