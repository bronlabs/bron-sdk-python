from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class message_for_signing(TypedDict, total=False):
    hashFunction: Optional[hash_function]
    keyType: Optional[key_type]
    message: Optional[str]
    signatureScheme: Optional[signature_scheme]
    signatureVariant: Optional[signature_variant]
