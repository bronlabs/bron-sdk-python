from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionEvents(TypedDict, total=False):
    events: List[TransactionEvent]
