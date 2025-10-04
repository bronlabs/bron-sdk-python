from enum import Enum


class IntentOrderStatus(Enum):
    NOT_EXIST = "not-exist"
    USER_INITIATED = "user-initiated"
    AUCTION_IN_PROGRESS = "auction-in-progress"
    WAIT_FOR_ORACLE_CONFIRM_USER_TX = "wait-for-oracle-confirm-user-tx"
    WAIT_FOR_SOLVER_TX = "wait-for-solver-tx"
    WAIT_FOR_ORACLE_CONFIRM_SOLVER_TX = "wait-for-oracle-confirm-solver-tx"
    COMPLETED = "completed"
    LIQUIDATED = "liquidated"
    CANCELLED = "cancelled"
