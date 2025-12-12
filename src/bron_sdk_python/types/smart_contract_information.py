from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class SmartContractInformation(TypedDict, total=False):
    contractAddress: Optional[str]
    standard: Optional[TokenStandard]
