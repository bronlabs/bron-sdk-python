from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.cancel_transaction import CancelTransaction
    from ..types.create_transaction import CreateTransaction
    from ..types.create_transactions import CreateTransactions
    from ..types.dry_run_transaction import DryRunTransaction
    from ..types.get_transactions_query import GetTransactionsQuery
    from ..types.offer_actions import OfferActions
    from ..types.transaction import Transaction
    from ..types.transaction_events import TransactionEvents
    from ..types.transactions import Transactions

class TransactionsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_transactions(self, query: Optional[GetTransactionsQuery] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transactions", await self._http.request(method='GET', path=path, query=query))

    async def create_transaction(self, body: Optional[CreateTransaction] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def create_multiple_transactions(self, body: Optional[CreateTransactions] = None) -> "Transactions":
        path = "/workspaces/{ws}/transactions/bulk-create"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transactions", await self._http.request(method='POST', path=path, body=body))

    async def dry_run_transaction(self, body: Optional[CreateTransaction] = None) -> "DryRunTransaction":
        path = "/workspaces/{ws}/transactions/dry-run"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("DryRunTransaction", await self._http.request(method='POST', path=path, body=body))

    async def get_transaction_by_id(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='GET', path=path))

    async def accept_deposit_offer(self, transactionId: str, body: Optional[OfferActions] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/accept-deposit-offer"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def cancel_transaction(self, transactionId: str, body: Optional[CancelTransaction] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/cancel"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

    async def create_signing_request(self, transactionId: str) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/create-signing-request"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path))

    async def get_transaction_events(self, transactionId: str) -> "TransactionEvents":
        path = "/workspaces/{ws}/transactions/{transactionId}/events"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("TransactionEvents", await self._http.request(method='GET', path=path))

    async def reject_outgoing_offer(self, transactionId: str, body: Optional[OfferActions] = None) -> "Transaction":
        path = "/workspaces/{ws}/transactions/{transactionId}/reject-outgoing-offer"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Transaction", await self._http.request(method='POST', path=path, body=body))

