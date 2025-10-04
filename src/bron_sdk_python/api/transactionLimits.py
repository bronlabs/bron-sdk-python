from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.get_transaction_limits_query import GetTransactionLimitsQuery
    from ..types.transaction_limit import TransactionLimit
    from ..types.transaction_limits import TransactionLimits

class TransactionLimitsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_transaction_limits(self, query: Optional[GetTransactionLimitsQuery] = None) -> "TransactionLimits":
        path = "/workspaces/{ws}/transaction-limits"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("TransactionLimits", await self._http.request(method='GET', path=path, query=query))

    async def get_transaction_limit_by_id(self, limitId: str) -> "TransactionLimit":
        path = "/workspaces/{ws}/transaction-limits/{limitId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("TransactionLimit", await self._http.request(method='GET', path=path))

