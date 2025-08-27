from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Stakes import Stakes

class StakeAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getStakes(self, query: Optional[dict] = None) -> "Stakes":
        path = "/workspaces/{ws}/stakes"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

