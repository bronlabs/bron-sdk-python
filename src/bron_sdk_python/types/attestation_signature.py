from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class AttestationSignature(TypedDict, total=False):
    publicKey: Optional[str]
    signature: Optional[str]
