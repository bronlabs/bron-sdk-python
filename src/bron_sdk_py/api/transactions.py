from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Transaction import Transaction
    from ..types.Transactions import Transactions

class TransactionsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getTransactions(self, query: Optional[dict] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def createTransaction(self, body: Optional[dict] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path, body=body)

    async def createMultipleTransactions(self, body: Optional[dict] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions/bulk-create"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path, body=body)

    async def dryRunTransaction(self, body: Optional[dict] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/dry-run"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path, body=body)

    async def getTransactionById(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path)

    async def cancelTransaction(self, transactionId: str, body: Optional[dict] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/cancel"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path, body=body)

    async def createSigningRequest(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/create-signing-request"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='POST', path=path)

