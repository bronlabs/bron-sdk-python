from enum import Enum


class transaction_limit_status(Enum):
    NEW = "new"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"
    DECLINED = "declined"
