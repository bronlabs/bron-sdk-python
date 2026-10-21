from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class TransactionEmbedded(TypedDict, total=False):
    attestationSignature: Optional[AttestationSignature]
    currentSigningRequest: Optional[SigningRequest]
    events: Optional[List[TransactionEvent]]
    intentsQuote: Optional[IntentsQuoteEmbedded]
    quoteDetails: Optional[QuoteDetails]
