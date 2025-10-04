from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.addresses import Addresses
    from ..types.get_deposit_addresses_query import GetDepositAddressesQuery

class AddressesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_deposit_addresses(self, query: Optional[GetDepositAddressesQuery] = None) -> "Addresses":
        path = "/workspaces/{ws}/addresses"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Addresses", await self._http.request(method='GET', path=path, query=query))

