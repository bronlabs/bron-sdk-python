from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Asset import Asset
    from ..types.Assets import Assets
    from ..types.Network import Network
    from ..types.Networks import Networks
    from ..types.Symbol import Symbol
    from ..types.SymbolMarketPrices import SymbolMarketPrices
    from ..types.Symbols import Symbols

class AssetsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getAssets(self, query: Optional[dict] = None) -> "Assets":
        path = "/dictionary/assets"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getAssetById(self, assetId: str, query: Optional[dict] = None) -> "Asset":
        path = "/dictionary/assets/{assetId}"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getNetworks(self, query: Optional[dict] = None) -> "Networks":
        path = "/dictionary/networks"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getNetworkById(self, networkId: str) -> "Network":
        path = "/dictionary/networks/{networkId}"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path)

    async def getPrices(self, query: Optional[dict] = None) -> "SymbolMarketPrices":
        path = "/dictionary/symbol-market-prices"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getSymbols(self, query: Optional[dict] = None) -> "Symbols":
        path = "/dictionary/symbols"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getSymbolById(self, symbolId: str, query: Optional[dict] = None) -> "Symbol":
        path = "/dictionary/symbols/{symbolId}"
        path = path.format(**locals())
        return await self._http.request(method='GET', path=path, query=query)

