from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class activity(TypedDict, total=False):
    accountId: Optional[str]
    activityId: str
    activityType: activity_type
    createdAt: str
    description: Optional[str]
    title: str
    userId: Optional[str]
    workspaceId: Optional[str]
