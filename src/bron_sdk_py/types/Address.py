from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class address(TypedDict, total=False):
    acceptsAllAssets: bool
    accountId: Optional[str]
    accountType: account_type
    activatedAssets: Optional[List[activated_asset]]
    address: Optional[str]
    addressId: str
    createdAt: str
    createdBy: str
    externalId: str
    memo: Optional[str]
    metadata: Optional[Dict[str, Any]]
    networkId: str
    requiresAssetsActivation: bool
    status: address_status
    updatedAt: str
    updatedBy: str
    workspaceId: Optional[str]
