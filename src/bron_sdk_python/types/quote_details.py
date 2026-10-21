from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class QuoteDetails(TypedDict, total=False):
    approvalAddress: Optional[str]
    expiresAt: Optional[str]
    fromAmount: Optional[str]
    fromAmountUSD: Optional[str]
    isCrossChain: Optional[bool]
    networkFee: Optional[str]
    networkFeeAssetId: Optional[str]
    networkFeeUSD: Optional[str]
    processingTime: Optional[str]
    provider: Optional[str]
    quoteId: Optional[str]
    serviceFeeUSD: Optional[str]
    slippage: Optional[str]
    toAmount: Optional[str]
    toAmountMin: Optional[str]
    toAmountUSD: Optional[str]
