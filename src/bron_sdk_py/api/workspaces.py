from typing import Optional, TYPE_CHECKING
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Activities import Activities
    from ..types.Workspace import Workspace
    from ..types.WorkspaceMembers import WorkspaceMembers

class WorkspacesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getWorkspaceById(self, query: Optional[dict] = None) -> "Workspace":
        path = "/workspaces/{ws}"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getActivities(self, query: Optional[dict] = None) -> "Activities":
        path = "/workspaces/{ws}/activities"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

    async def getWorkspaceMembers(self, query: Optional[dict] = None) -> "WorkspaceMembers":
        path = "/workspaces/{ws}/members"
        path = path.format(ws=self._workspace_id, **locals())
        return await self._http.request(method='GET', path=path, query=query)

