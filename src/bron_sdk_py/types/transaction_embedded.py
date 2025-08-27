from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class transaction_embedded(TypedDict, total=False):
    currentSigningRequest: Optional[signing_request]
