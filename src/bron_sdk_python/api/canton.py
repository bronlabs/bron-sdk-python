from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.canton_ledger_query import CantonLedgerQuery
    from ..types.canton_ledger_query_result import CantonLedgerQueryResult

class CantonAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def canton_ledger_api_passthrough(self, body: Optional[CantonLedgerQuery] = None) -> "CantonLedgerQueryResult":
        path = "/workspaces/{ws}/canton/ledger-query"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("CantonLedgerQueryResult", await self._http.request(method='POST', path=path, body=body))

