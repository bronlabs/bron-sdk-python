from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.balance import Balance
    from ..types.balances import Balances
    from ..types.get_balances_query import GetBalancesQuery

class BalancesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_balances(self, query: Optional[GetBalancesQuery] = None) -> "Balances":
        path = "/workspaces/{ws}/balances"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Balances", await self._http.request(method='GET', path=path, query=query))

    async def get_balance_by_id(self, balanceId: str) -> "Balance":
        path = "/workspaces/{ws}/balances/{balanceId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Balance", await self._http.request(method='GET', path=path))

