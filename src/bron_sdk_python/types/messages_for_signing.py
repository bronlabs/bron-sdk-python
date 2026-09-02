from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class MessagesForSigning(TypedDict, total=False):
    messages: Optional[List[MessageForSigning]]
    parallelSigning: Optional[bool]
    primitivesVersion: Optional[str]
    publicKey: Optional[str]
    useBackupPrimitive: Optional[bool]
