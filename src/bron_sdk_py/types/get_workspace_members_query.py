from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_workspace_members_query(TypedDict, total=False):
    includePermissionGroups: Optional[bool]
    includeUsersProfiles: Optional[bool]
    includeEmails: Optional[bool]
