from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.cancel_transaction import cancel_transaction
    from ..types.create_transaction import create_transaction
    from ..types.create_transactions import create_transactions
    from ..types.get_transactions_query import get_transactions_query
    from ..types.transaction import transaction
    from ..types.transactions import transactions

class TransactionsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_transactions(self, query: Optional[get_transactions_query] = None) -> "transactions":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transactions", await self._http.request(method='GET', path=path, query=query))

    async def create_transaction(self, body: Optional[create_transaction] = None) -> "transaction":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction", await self._http.request(method='POST', path=path, body=body))

    async def create_multiple_transactions(self, body: Optional[create_transactions] = None) -> "transactions":
        path = "/workspaces/{ws}/transactions/bulk-create"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transactions", await self._http.request(method='POST', path=path, body=body))

    async def dry_run_transaction(self, body: Optional[create_transaction] = None) -> "transaction":
        path = "/workspaces/{ws}/transactions/dry-run"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction", await self._http.request(method='POST', path=path, body=body))

    async def get_transaction_by_id(self, transactionId: str) -> "transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction", await self._http.request(method='GET', path=path))

    async def cancel_transaction(self, transactionId: str, body: Optional[cancel_transaction] = None) -> "transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/cancel"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction", await self._http.request(method='POST', path=path, body=body))

    async def create_signing_request(self, transactionId: str) -> "transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/create-signing-request"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("transaction", await self._http.request(method='POST', path=path))

