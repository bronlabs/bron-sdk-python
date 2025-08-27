from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Addresses import Addresses
    from ..types.AddressessQuery import AddressessQuery

class AddressesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getDepositAddresses(self, query: Optional[AddressessQuery] = None) -> "Addresses":
        path = "/workspaces/{ws}/addresses"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Addresses", await self._http.request(method='GET', path=path, query=query))

