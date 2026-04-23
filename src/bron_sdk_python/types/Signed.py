from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Signed(TypedDict, total=False):
    signature: Optional[str]
    signatures: Optional[List[Signature]]
