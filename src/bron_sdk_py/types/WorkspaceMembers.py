from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class WorkspaceMembers(TypedDict, total=False):
    members: List[WorkspaceMember]
