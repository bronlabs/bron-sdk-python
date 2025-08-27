from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.address_book_record import address_book_record
    from ..types.address_book_records import address_book_records
    from ..types.create_address_book_record import create_address_book_record
    from ..types.get_address_book_records_query import get_address_book_records_query
    from ..types.unit import unit

class AddressBookAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_address_book_records(self, query: Optional[get_address_book_records_query] = None) -> "address_book_records":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("address_book_records", await self._http.request(method='GET', path=path, query=query))

    async def create_address_book_record(self, body: Optional[create_address_book_record] = None) -> "address_book_record":
        path = "/workspaces/{ws}/address-book-records"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("address_book_record", await self._http.request(method='POST', path=path, body=body))

    async def deactivate_address_book_record(self, recordId: str) -> "unit":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("unit", await self._http.request(method='DELETE', path=path))

    async def get_address_book_record_by_id(self, recordId: str) -> "address_book_record":
        path = "/workspaces/{ws}/address-book-records/{recordId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("address_book_record", await self._http.request(method='GET', path=path))

