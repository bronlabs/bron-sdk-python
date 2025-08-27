from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class limit_rule(TypedDict, total=False):
    approve: Optional[limit_rule_approve]
    securityDelay: Optional[limit_rule_security_delay]
    skipApproval: Optional[bool]
