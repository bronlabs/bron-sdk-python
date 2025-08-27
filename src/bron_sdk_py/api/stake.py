from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.get_stakes_query import get_stakes_query
    from ..types.stakes import stakes

class StakeAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_stakes(self, query: Optional[get_stakes_query] = None) -> "stakes":
        path = "/workspaces/{ws}/stakes"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("stakes", await self._http.request(method='GET', path=path, query=query))

