from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.get_transaction_limits_query import get_transaction_limits_query
    from ..types.transaction_limit import transaction_limit
    from ..types.transaction_limits import transaction_limits

class TransactionLimitsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_transaction_limits(self, query: Optional[get_transaction_limits_query] = None) -> "transaction_limits":
        path = "/workspaces/{ws}/transaction-limits"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction_limits", await self._http.request(method='GET', path=path, query=query))

    async def get_transaction_limit_by_id(self, limitId: str) -> "transaction_limit":
        path = "/workspaces/{ws}/transaction-limits/{limitId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction_limit", await self._http.request(method='GET', path=path))

