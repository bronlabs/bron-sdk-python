from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatInReceived(TypedDict, total=False):
    fiatAmount: Optional[str]
    reference: Optional[str]
    senderAccountNumber: Optional[str]
    senderName: Optional[str]
