from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.balance import balance
    from ..types.balances import balances
    from ..types.get_balances_query import get_balances_query

class BalancesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_balances(self, query: Optional[get_balances_query] = None) -> "balances":
        path = "/workspaces/{ws}/balances"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("balances", await self._http.request(method='GET', path=path, query=query))

    async def get_balance_by_id(self, balanceId: str) -> "balance":
        path = "/workspaces/{ws}/balances/{balanceId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("balance", await self._http.request(method='GET', path=path))

