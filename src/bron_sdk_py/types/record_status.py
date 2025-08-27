from enum import Enum


class record_status(Enum):
    NEW = "new"
    ACTIVE = "active"
    REJECTED = "rejected"
    DELETED = "deleted"
