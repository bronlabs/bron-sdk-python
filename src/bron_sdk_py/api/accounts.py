from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Account import Account
    from ..types.Accounts import Accounts

class AccountsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getAccounts(self, query: Optional[dict] = None) -> "Accounts":
        path = "/workspaces/{ws}/accounts"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getAccountById(self, accountId: str) -> "Account":
        path = "/workspaces/{ws}/accounts/{accountId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path)

