from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.create_intent import CreateIntent
    from ..types.intent import Intent
    from ..types.intents_quote import IntentsQuote
    from ..types.request_indicative_swap_quote_query import RequestIndicativeSwapQuoteQuery

class IntentsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def create_intent_request(self, body: Optional[CreateIntent] = None) -> "Intent":
        path = "/workspaces/{ws}/intents"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Intent", await self._http.request(method='POST', path=path, body=body))

    async def request_indicative_swap_quote(self, query: Optional[RequestIndicativeSwapQuoteQuery] = None) -> "IntentsQuote":
        path = "/workspaces/{ws}/intents/quote"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("IntentsQuote", await self._http.request(method='POST', path=path, query=query))

    async def get_intent_request_by_id(self, intentId: str) -> "Intent":
        path = "/workspaces/{ws}/intents/{intentId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Intent", await self._http.request(method='GET', path=path))

