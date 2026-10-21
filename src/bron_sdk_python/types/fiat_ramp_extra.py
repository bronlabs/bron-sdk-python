from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatRampExtra(TypedDict, total=False):
    amount: Optional[str]
    bankDetails: Optional[FiatInBankDetails]
    fiatAmount: Optional[str]
    fiatInReceived: Optional[FiatInReceived]
    platformFee: Optional[str]
    provider: Optional[str]
    providerFee: Optional[str]
    rate: Optional[str]
