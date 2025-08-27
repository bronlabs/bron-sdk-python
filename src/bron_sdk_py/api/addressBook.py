from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.AddressBookRecord import AddressBookRecord
    from ..types.AddressBookRecords import AddressBookRecords
    from ..types.Unit import Unit

class AddressBookAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getAddressBookRecords(self, query: Optional[dict] = None) -> "AddressBookRecords":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def createAddressBookRecord(self, body: Optional[dict] = None) -> "AddressBookRecord":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path, body=body)

    async def deactivateAddressBookRecord(self, recordId: str) -> "Unit":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='DELETE', path=path)

    async def getAddressBookRecordById(self, recordId: str) -> "AddressBookRecord":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path)

