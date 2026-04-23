from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatExchangeParams(TypedDict, total=False):
    amount: str
    feeLevel: Optional[FeeLevel]
    fromAccountId: Optional[str]
    fromAssetId: str
    fromBankAccountId: Optional[str]
    fromNetworkId: str
    toAccountId: Optional[str]
    toAssetId: str
    toBankAccountId: Optional[str]
    toNetworkId: str
