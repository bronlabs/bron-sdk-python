from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Balance import Balance
    from ..types.Balances import Balances
    from ..types.BalancessQuery import BalancessQuery

class BalancesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getBalances(self, query: Optional[BalancessQuery] = None) -> "Balances":
        path = "/workspaces/{ws}/balances"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Balances", await self._http.request(method='GET', path=path, query=query))

    async def getBalanceById(self, balanceId: str) -> "Balance":
        path = "/workspaces/{ws}/balances/{balanceId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Balance", await self._http.request(method='GET', path=path))

