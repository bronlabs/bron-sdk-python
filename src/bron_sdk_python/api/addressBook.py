from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.address_book_record import AddressBookRecord
    from ..types.address_book_records import AddressBookRecords
    from ..types.create_address_book_record import CreateAddressBookRecord
    from ..types.get_address_book_records_query import GetAddressBookRecordsQuery
    from ..types.unit import Unit

class AddressBookAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_address_book_records(self, query: Optional[GetAddressBookRecordsQuery] = None) -> "AddressBookRecords":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("AddressBookRecords", await self._http.request(method='GET', path=path, query=query))

    async def create_address_book_record(self, body: Optional[CreateAddressBookRecord] = None) -> "AddressBookRecord":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("AddressBookRecord", await self._http.request(method='POST', path=path, body=body))

    async def deactivate_address_book_record(self, recordId: str) -> "Unit":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Unit", await self._http.request(method='DELETE', path=path))

    async def get_address_book_record_by_id(self, recordId: str) -> "AddressBookRecord":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("AddressBookRecord", await self._http.request(method='GET', path=path))

