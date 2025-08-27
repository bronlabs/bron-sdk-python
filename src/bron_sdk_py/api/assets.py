from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.asset import asset
    from ..types.assets import assets
    from ..types.get_asset_by_id_query import get_asset_by_id_query
    from ..types.get_assets_query import get_assets_query
    from ..types.get_networks_query import get_networks_query
    from ..types.get_prices_query import get_prices_query
    from ..types.get_symbol_by_id_query import get_symbol_by_id_query
    from ..types.get_symbols_query import get_symbols_query
    from ..types.network import network
    from ..types.networks import networks
    from ..types.symbol import symbol
    from ..types.symbol_market_prices import symbol_market_prices
    from ..types.symbols import symbols

class AssetsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_assets(self, query: Optional[get_assets_query] = None) -> "assets":
        path = "/dictionary/assets"
        path = path.format(**locals())
        return cast("assets", await self._http.request(method='GET', path=path, query=query))

    async def get_asset_by_id(self, assetId: str, query: Optional[get_asset_by_id_query] = None) -> "asset":
        path = "/dictionary/assets/{assetId}"
        path = path.format(**locals())
        return cast("asset", await self._http.request(method='GET', path=path, query=query))

    async def get_networks(self, query: Optional[get_networks_query] = None) -> "networks":
        path = "/dictionary/networks"
        path = path.format(**locals())
        return cast("networks", await self._http.request(method='GET', path=path, query=query))

    async def get_network_by_id(self, networkId: str) -> "network":
        path = "/dictionary/networks/{networkId}"
        path = path.format(**locals())
        return cast("network", await self._http.request(method='GET', path=path))

    async def get_prices(self, query: Optional[get_prices_query] = None) -> "symbol_market_prices":
        path = "/dictionary/symbol-market-prices"
        path = path.format(**locals())
        return cast("symbol_market_prices", await self._http.request(method='GET', path=path, query=query))

    async def get_symbols(self, query: Optional[get_symbols_query] = None) -> "symbols":
        path = "/dictionary/symbols"
        path = path.format(**locals())
        return cast("symbols", await self._http.request(method='GET', path=path, query=query))

    async def get_symbol_by_id(self, symbolId: str, query: Optional[get_symbol_by_id_query] = None) -> "symbol":
        path = "/dictionary/symbols/{symbolId}"
        path = path.format(**locals())
        return cast("symbol", await self._http.request(method='GET', path=path, query=query))

