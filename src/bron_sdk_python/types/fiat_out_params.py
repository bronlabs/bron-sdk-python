from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatOutParams(TypedDict, total=False):
    amount: Optional[str]
    assetId: str
    feeLevel: Optional[FeeLevel]
    fiatAmount: Optional[str]
    fiatAssetId: str
    paymentPurpose: Optional[str]
    processingTier: Optional[str]
    reference: Optional[str]
    toAddressBookRecordId: str
