from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SigningMessage(TypedDict, total=False):
    message: str
    version: Optional[str]
