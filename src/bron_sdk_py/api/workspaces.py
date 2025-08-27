from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.Activities import Activities
    from ..types.Workspace import Workspace
    from ..types.WorkspaceMembers import WorkspaceMembers
    from ..types.WorkspacessQuery import WorkspacessQuery

class WorkspacesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def getWorkspaceById(self, query: Optional[WorkspacessQuery] = None) -> "Workspace":
        path = "/workspaces/{ws}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Workspace", await self._http.request(method='GET', path=path, query=query))

    async def getActivities(self, query: Optional[WorkspacessQuery] = None) -> "Activities":
        path = "/workspaces/{ws}/activities"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Activities", await self._http.request(method='GET', path=path, query=query))

    async def getWorkspaceMembers(self, query: Optional[WorkspacessQuery] = None) -> "WorkspaceMembers":
        path = "/workspaces/{ws}/members"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("WorkspaceMembers", await self._http.request(method='GET', path=path, query=query))

