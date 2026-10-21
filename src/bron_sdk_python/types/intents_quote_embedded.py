from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class IntentsQuoteEmbedded(TypedDict, total=False):
    slippageBps: Optional[str]
    slippageReason: Optional[SlippageReason]
    stockSession: Optional[StockSession]
