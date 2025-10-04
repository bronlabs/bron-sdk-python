from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class MessageForSigning(TypedDict, total=False):
    hashFunction: Optional[HashFunction]
    keyType: Optional[KeyType]
    message: Optional[str]
    signatureScheme: Optional[SignatureScheme]
    signatureVariant: Optional[SignatureVariant]
