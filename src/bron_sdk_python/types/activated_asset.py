from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class ActivatedAsset(TypedDict, total=False):
    activationId: Optional[str]
    address: Optional[str]
    assetId: Optional[str]
    status: Optional[AddressStatus]
