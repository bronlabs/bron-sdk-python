from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class get_activities_query(TypedDict, total=False):
    accountIds: Optional[List[str]]
    offset: Optional[str]
    limit: Optional[str]
    search: Optional[str]
    userIds: Optional[List[str]]
    activityTypes: Optional[List[activity_type]]
    excludedActivityTypes: Optional[List[activity_type]]
