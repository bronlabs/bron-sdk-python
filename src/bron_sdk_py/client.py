from __future__ import annotations

from .utils.http import HttpClient


class BronClient:
    def __init__(self, *, api_key: str, workspace_id: str, base_url: str = "https://api.bron.org", timeout: float | None = None):
        effective_base_url = base_url.strip() or "https://api.bron.org"
        http = HttpClient(effective_base_url, api_key, timeout=timeout)
        self.workspace_id = workspace_id

        # API namespaces will be generated into .api package
        from .api.accounts import AccountsAPI
        from .api.balances import BalancesAPI
        from .api.transactions import TransactionsAPI
        from .api.addresses import AddressesAPI
        from .api.assets import AssetsAPI
        from .api.workspaces import WorkspacesAPI
        from .api.transactionLimits import TransactionLimitsAPI
        from .api.addressBook import AddressBookAPI
        from .api.stake import StakeAPI

        self.accounts = AccountsAPI(http, workspace_id)
        self.balances = BalancesAPI(http, workspace_id)
        self.transactions = TransactionsAPI(http, workspace_id)
        self.addresses = AddressesAPI(http, workspace_id)
        self.assets = AssetsAPI(http)
        self.workspaces = WorkspacesAPI(http, workspace_id)
        self.transactionLimits = TransactionLimitsAPI(http, workspace_id)
        self.addressBook = AddressBookAPI(http, workspace_id)
        self.stake = StakeAPI(http, workspace_id)

        self._http = http

    async def aclose(self) -> None:
        await self._http.aclose()


