from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Balance import Balance
    from ..types.Balances import Balances

class BalancesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getBalances(self, query: Optional[dict] = None) -> "Balances":
        path = "/workspaces/{ws}/balances"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getBalanceById(self, balanceId: str) -> "Balance":
        path = "/workspaces/{ws}/balances/{balanceId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path)

