from __future__ import annotations
from typing import Optional, TYPE_CHECKING, cast
from ..utils.http import HttpClient
if TYPE_CHECKING:
    from ..types.create_intent import CreateIntent
    from ..types.get_indicative_quote_for_an_intent_swap_pair_query import GetIndicativeQuoteForAnIntentSwapPairQuery
    from ..types.intent import Intent
    from ..types.intents_quote import IntentsQuote
    from ..types.public_intent_pairs import PublicIntentPairs

class IntentsAPI:
    def __init__(self, http: HttpClient, workspace_id: Optional[str] = None) -> None:
        self._http = http
        self._workspace_id = workspace_id

    async def get_intent_swap_pairs(self) -> "PublicIntentPairs":
        path = "/dictionary/intent-pairs"
        path = path.format(**locals())
        return cast("PublicIntentPairs", await self._http.request(method='GET', path=path))

    async def get_indicative_quote_for_an_intent_swap_pair(self, fromAssetId: str, toAssetId: str, query: Optional[GetIndicativeQuoteForAnIntentSwapPairQuery] = None) -> "IntentsQuote":
        path = "/dictionary/intent-pairs/{fromAssetId}/{toAssetId}/quote"
        path = path.format(**locals())
        return cast("IntentsQuote", await self._http.request(method='GET', path=path, query=query))

    async def create_intent_request(self, body: Optional[CreateIntent] = None) -> "Intent":
        path = "/workspaces/{ws}/intents"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Intent", await self._http.request(method='POST', path=path, body=body))

    async def get_intent_request_by_id(self, intentId: str) -> "Intent":
        path = "/workspaces/{ws}/intents/{intentId}"
        path = path.format(ws=self._workspace_id, **locals())
        return cast("Intent", await self._http.request(method='GET', path=path))

