from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class RecreateSigningRequest(TypedDict, total=False):
    cancelTransaction: Optional[bool]
    feeLevel: Optional[FeeLevel]
    networkFees: Optional[RequestedNetworkFees]
    primitivesVersion: Optional[str]
    signingRequestId: str
