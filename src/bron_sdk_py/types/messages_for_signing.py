from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class messages_for_signing(TypedDict, total=False):
    messages: Optional[List[message_for_signing]]
    publicKey: Optional[str]
    useBackupPrimitive: Optional[bool]
