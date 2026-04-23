from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatOutParams(TypedDict, total=False):
    amount: str
    assetId: str
    feeLevel: Optional[FeeLevel]
    fiatAssetId: str
    networkId: str
    toAddressBookRecordId: str
