from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.CancelTransaction import CancelTransaction
    from ..types.CreateTransaction import CreateTransaction
    from ..types.CreateTransactions import CreateTransactions
    from ..types.Transaction import Transaction
    from ..types.Transactions import Transactions
    from ..types.TransactionssQuery import TransactionssQuery

class TransactionsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getTransactions(self, query: Optional[TransactionssQuery] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transactions", await self._http.request(method='GET', path=path, query=query))

    async def createTransaction(self, body: Optional[CreateTransaction] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def createMultipleTransactions(self, body: Optional[CreateTransactions] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions/bulk-create"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transactions", await self._http.request(method='POST', path=path, body=body))

    async def dryRunTransaction(self, body: Optional[CreateTransaction] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/dry-run"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def getTransactionById(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='GET', path=path))

    async def cancelTransaction(self, transactionId: str, body: Optional[CancelTransaction] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/cancel"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def createSigningRequest(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/create-signing-request"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path))

