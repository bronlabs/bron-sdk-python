from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Identity(TypedDict, total=False):
    createdAt: str
    createdBy: Optional[str]
    expiresAt: Optional[str]
    identityId: str
    identityType: IdentityType
    identityValue: str
    lastUsedAt: Optional[str]
    updatedAt: Optional[str]
    userId: str
