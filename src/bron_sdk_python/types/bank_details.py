from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class BankDetails(TypedDict, total=False):
    accountHolderType: AccountHolderType
    accountNumber: str
    accountType: Optional[BankAccountType]
    bankAddress: Optional[BankAddress]
    bankCode: Optional[str]
    businessName: Optional[str]
    businessRegistrationNumber: Optional[str]
    channelType: BankChannelType
    correspondentBankCode: Optional[str]
    country: str
    fiatCurrency: str
    firstName: Optional[str]
    issuer: str
    lastName: Optional[str]
    paymentPurpose: Optional[str]
    reference: Optional[str]
    registeredAddress: Optional[str]
