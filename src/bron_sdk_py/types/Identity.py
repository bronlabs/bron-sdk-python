from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class identity(TypedDict, total=False):
    createdAt: str
    createdBy: Optional[str]
    identityId: str
    identityType: identity_type
    identityValue: str
    lastUsedAt: Optional[str]
    updatedAt: Optional[str]
    userId: str
