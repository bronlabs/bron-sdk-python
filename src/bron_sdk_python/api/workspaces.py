from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.activities import Activities
    from ..types.get_activities_query import GetActivitiesQuery
    from ..types.get_workspace_by_id_query import GetWorkspaceByIdQuery
    from ..types.get_workspace_members_query import GetWorkspaceMembersQuery
    from ..types.workspace import Workspace
    from ..types.workspace_members import WorkspaceMembers

class WorkspacesAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_workspace_by_id(self, query: Optional[GetWorkspaceByIdQuery] = None) -> "Workspace":
        path = "/workspaces/{ws}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Workspace", await self._http.request(method='GET', path=path, query=query))

    async def get_activities(self, query: Optional[GetActivitiesQuery] = None) -> "Activities":
        path = "/workspaces/{ws}/activities"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Activities", await self._http.request(method='GET', path=path, query=query))

    async def get_workspace_members(self, query: Optional[GetWorkspaceMembersQuery] = None) -> "WorkspaceMembers":
        path = "/workspaces/{ws}/members"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("WorkspaceMembers", await self._http.request(method='GET', path=path, query=query))

