from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Asset import Asset
    from ..types.Assets import Assets
    from ..types.AssetssQuery import AssetssQuery
    from ..types.Network import Network
    from ..types.Networks import Networks
    from ..types.Symbol import Symbol
    from ..types.SymbolMarketPrices import SymbolMarketPrices
    from ..types.Symbols import Symbols

class AssetsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getAssets(self, query: Optional[AssetssQuery] = None) -> "Assets":
        path = "/dictionary/assets"
        path = path.format(**locals())
        return cast("Assets", await self._http.request(method='GET', path=path, query=query))

    async def getAssetById(self, assetId: str, query: Optional[AssetssQuery] = None) -> "Asset":
        path = "/dictionary/assets/{assetId}"
        path = path.format(**locals())
        return cast("Asset", await self._http.request(method='GET', path=path, query=query))

    async def getNetworks(self, query: Optional[AssetssQuery] = None) -> "Networks":
        path = "/dictionary/networks"
        path = path.format(**locals())
        return cast("Networks", await self._http.request(method='GET', path=path, query=query))

    async def getNetworkById(self, networkId: str) -> "Network":
        path = "/dictionary/networks/{networkId}"
        path = path.format(**locals())
        return cast("Network", await self._http.request(method='GET', path=path))

    async def getPrices(self, query: Optional[AssetssQuery] = None) -> "SymbolMarketPrices":
        path = "/dictionary/symbol-market-prices"
        path = path.format(**locals())
        return cast("SymbolMarketPrices", await self._http.request(method='GET', path=path, query=query))

    async def getSymbols(self, query: Optional[AssetssQuery] = None) -> "Symbols":
        path = "/dictionary/symbols"
        path = path.format(**locals())
        return cast("Symbols", await self._http.request(method='GET', path=path, query=query))

    async def getSymbolById(self, symbolId: str, query: Optional[AssetssQuery] = None) -> "Symbol":
        path = "/dictionary/symbols/{symbolId}"
        path = path.format(**locals())
        return cast("Symbol", await self._http.request(method='GET', path=path, query=query))

