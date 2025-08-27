from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.account import account
    from ..types.accounts import accounts
    from ..types.get_accounts_query import get_accounts_query

class AccountsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_accounts(self, query: Optional[get_accounts_query] = None) -> "accounts":
        path = "/workspaces/{ws}/accounts"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("accounts", await self._http.request(method='GET', path=path, query=query))

    async def get_account_by_id(self, accountId: str) -> "account":
        path = "/workspaces/{ws}/accounts/{accountId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("account", await self._http.request(method='GET', path=path))

