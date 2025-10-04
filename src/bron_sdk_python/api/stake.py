from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.get_stakes_query import GetStakesQuery
    from ..types.stakes import Stakes

class StakeAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_stakes(self, query: Optional[GetStakesQuery] = None) -> "Stakes":
        path = "/workspaces/{ws}/stakes"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Stakes", await self._http.request(method='GET', path=path, query=query))

