from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class WorkspacessQuery(TypedDict, total=False):
    workspaceIds: Optional[List[str]]
    includeSettings: Optional[bool]
    limit: Optional[str]
    offset: Optional[str]
    accountIds: Optional[List[str]]
    search: Optional[str]
    userIds: Optional[List[str]]
    activityTypes: Optional[List[ActivityType]]
    excludedActivityTypes: Optional[List[ActivityType]]
    includePermissionGroups: Optional[bool]
    includeUsersProfiles: Optional[bool]
    includeEmails: Optional[bool]
