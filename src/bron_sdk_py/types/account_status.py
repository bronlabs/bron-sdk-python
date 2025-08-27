from enum import Enum


class account_status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    SHARD_GENERATING = "shard-generating"
