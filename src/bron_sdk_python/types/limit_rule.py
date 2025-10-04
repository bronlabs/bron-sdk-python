from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class LimitRule(TypedDict, total=False):
    approve: Optional[LimitRuleApprove]
    securityDelay: Optional[LimitRuleSecurityDelay]
    skipApproval: Optional[bool]
