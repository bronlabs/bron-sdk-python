from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class requested_network_fees(TypedDict, total=False):
    feePerByte: Optional[str]
    gasLimit: Optional[str]
    gasPriceGwei: Optional[str]
    maxFeePerGas: Optional[str]
    maxPriorityFeePerGas: Optional[str]
