from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionEmbedded(TypedDict, total=False):
    currentSigningRequest: Optional[SigningRequest]
    events: Optional[List[TransactionEvent]]
