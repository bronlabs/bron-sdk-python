from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.activities import activities
    from ..types.get_activities_query import get_activities_query
    from ..types.get_workspace_by_id_query import get_workspace_by_id_query
    from ..types.get_workspace_members_query import get_workspace_members_query
    from ..types.workspace import workspace
    from ..types.workspace_members import workspace_members

class WorkspacesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_workspace_by_id(self, query: Optional[get_workspace_by_id_query] = None) -> "workspace":
        path = "/workspaces/{ws}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("workspace", await self._http.request(method='GET', path=path, query=query))

    async def get_activities(self, query: Optional[get_activities_query] = None) -> "activities":
        path = "/workspaces/{ws}/activities"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("activities", await self._http.request(method='GET', path=path, query=query))

    async def get_workspace_members(self, query: Optional[get_workspace_members_query] = None) -> "workspace_members":
        path = "/workspaces/{ws}/members"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("workspace_members", await self._http.request(method='GET', path=path, query=query))

