from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class PublicIntentPair(TypedDict, total=False):
    assetA: IntentPairAsset
    assetB: IntentPairAsset
    isBidirectional: bool
