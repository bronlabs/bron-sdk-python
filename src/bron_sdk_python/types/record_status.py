from enum import Enum


class RecordStatus(Enum):
    NEW = "new"
    ACTIVE = "active"
    REJECTED = "rejected"
    DELETED = "deleted"
