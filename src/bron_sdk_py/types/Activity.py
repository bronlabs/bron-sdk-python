from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Activity(TypedDict, total=False):
    accountId: Optional[str]
    activityId: str
    activityType: ActivityType
    createdAt: str
    description: Optional[str]
    title: str
    userId: Optional[str]
    workspaceId: Optional[str]
