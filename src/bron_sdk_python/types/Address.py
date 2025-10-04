from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class Address(TypedDict, total=False):
    acceptsAllAssets: bool
    accountId: Optional[str]
    accountType: AccountType
    activatedAssets: Optional[List[ActivatedAsset]]
    address: Optional[str]
    addressId: str
    createdAt: str
    createdBy: str
    externalId: str
    memo: Optional[str]
    metadata: Optional[Dict[str, Any]]
    networkId: str
    requiresAssetsActivation: bool
    status: AddressStatus
    updatedAt: str
    updatedBy: str
    workspaceId: Optional[str]
