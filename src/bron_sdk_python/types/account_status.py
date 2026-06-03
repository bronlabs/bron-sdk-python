from enum import Enum


class AccountStatus(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    SHARD_GENERATING = "shard-generating"
    ERROR_ON_GENERATING = "error-on-generating"
