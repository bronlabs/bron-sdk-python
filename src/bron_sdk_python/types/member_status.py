from enum import Enum


class MemberStatus(Enum):
    NEW = "new"
    ACTIVE = "active"
    REJECTED = "rejected"
    DEACTIVATED = "deactivated"
