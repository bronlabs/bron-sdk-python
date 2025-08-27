from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class webhook_event(TypedDict, total=False):
    event: str
    eventId: str
    payload: Dict[str, Any]
    subscriptionId: str
