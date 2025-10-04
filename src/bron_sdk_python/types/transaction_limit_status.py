from enum import Enum


class TransactionLimitStatus(Enum):
    NEW = "new"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"
    DECLINED = "declined"
