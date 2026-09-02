from enum import Enum


class StakeStatus(Enum):
    BONDING = "bonding"
    ACTIVE = "active"
    UNBONDING = "unbonding"
    REQUIRE_CLAIM = "require-claim"
    EXITED = "exited"
