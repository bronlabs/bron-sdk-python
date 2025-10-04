from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class WorkspaceMemberEmbedded(TypedDict, total=False):
    identities: Optional[List[Identity]]
    permissionGroups: Optional[List[str]]
    profile: Optional[UserProfile]
