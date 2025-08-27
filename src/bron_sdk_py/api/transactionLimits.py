from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.TransactionLimit import TransactionLimit
    from ..types.TransactionLimits import TransactionLimits
    from ..types.TransactionLimitssQuery import TransactionLimitssQuery

class TransactionLimitsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getTransactionLimits(self, query: Optional[TransactionLimitssQuery] = None) -> "TransactionLimits":
        path = "/workspaces/{ws}/transaction-limits"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("TransactionLimits", await self._http.request(method='GET', path=path, query=query))

    async def getTransactionLimitById(self, limitId: str) -> "TransactionLimit":
        path = "/workspaces/{ws}/transaction-limits/{limitId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("TransactionLimit", await self._http.request(method='GET', path=path))

