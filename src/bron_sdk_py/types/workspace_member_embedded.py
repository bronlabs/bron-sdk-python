from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class workspace_member_embedded(TypedDict, total=False):
    identities: Optional[List[identity]]
    permissionGroups: Optional[List[str]]
    profile: Optional[user_profile]
