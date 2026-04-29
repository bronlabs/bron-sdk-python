from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.asset import Asset
    from ..types.asset_market_prices import AssetMarketPrices
    from ..types.assets import Assets
    from ..types.get_asset_by_id_query import GetAssetByIdQuery
    from ..types.get_asset_prices_query import GetAssetPricesQuery
    from ..types.get_assets_query import GetAssetsQuery
    from ..types.get_networks_query import GetNetworksQuery
    from ..types.get_prices_query import GetPricesQuery
    from ..types.get_symbol_by_id_query import GetSymbolByIdQuery
    from ..types.get_symbols_query import GetSymbolsQuery
    from ..types.network import Network
    from ..types.networks import Networks
    from ..types.symbol import Symbol
    from ..types.symbol_market_prices import SymbolMarketPrices
    from ..types.symbols import Symbols

class AssetsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_asset_prices(self, query: Optional[GetAssetPricesQuery] = None) -> "AssetMarketPrices":
        path = "/dictionary/asset-market-prices"
        path = path.format(**locals())
        return cast("AssetMarketPrices", await self._http.request(method='GET', path=path, query=query))

    async def get_assets(self, query: Optional[GetAssetsQuery] = None) -> "Assets":
        path = "/dictionary/assets"
        path = path.format(**locals())
        return cast("Assets", await self._http.request(method='GET', path=path, query=query))

    async def get_asset_by_id(self, assetId: str, query: Optional[GetAssetByIdQuery] = None) -> "Asset":
        path = "/dictionary/assets/{assetId}"
        path = path.format(**locals())
        return cast("Asset", await self._http.request(method='GET', path=path, query=query))

    async def get_networks(self, query: Optional[GetNetworksQuery] = None) -> "Networks":
        path = "/dictionary/networks"
        path = path.format(**locals())
        return cast("Networks", await self._http.request(method='GET', path=path, query=query))

    async def get_network_by_id(self, networkId: str) -> "Network":
        path = "/dictionary/networks/{networkId}"
        path = path.format(**locals())
        return cast("Network", await self._http.request(method='GET', path=path))

    async def get_prices(self, query: Optional[GetPricesQuery] = None) -> "SymbolMarketPrices":
        path = "/dictionary/symbol-market-prices"
        path = path.format(**locals())
        return cast("SymbolMarketPrices", await self._http.request(method='GET', path=path, query=query))

    async def get_symbols(self, query: Optional[GetSymbolsQuery] = None) -> "Symbols":
        path = "/dictionary/symbols"
        path = path.format(**locals())
        return cast("Symbols", await self._http.request(method='GET', path=path, query=query))

    async def get_symbol_by_id(self, symbolId: str, query: Optional[GetSymbolByIdQuery] = None) -> "Symbol":
        path = "/dictionary/symbols/{symbolId}"
        path = path.format(**locals())
        return cast("Symbol", await self._http.request(method='GET', path=path, query=query))

