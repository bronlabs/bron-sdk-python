from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class FiatInBankDetails(TypedDict, total=False):
    accountHolderName: Optional[str]
    accountNumber: Optional[str]
    bankAddress: Optional[BankAddress]
    bankCode: Optional[str]
    bankName: Optional[str]
    channelType: Optional[BankChannelType]
