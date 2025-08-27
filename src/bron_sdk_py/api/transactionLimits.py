from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.TransactionLimit import TransactionLimit
    from ..types.TransactionLimits import TransactionLimits

class TransactionLimitsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getTransactionLimits(self, query: Optional[dict] = None) -> "TransactionLimits":
        path = "/workspaces/{ws}/transaction-limits"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getTransactionLimitById(self, limitId: str) -> "TransactionLimit":
        path = "/workspaces/{ws}/transaction-limits/{limitId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path)

