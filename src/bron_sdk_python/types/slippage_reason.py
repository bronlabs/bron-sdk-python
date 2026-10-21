from enum import Enum


class SlippageReason(Enum):
    STOCK_OFF_SESSION = "stock-off-session"
    STOCK_SESSION_UNKNOWN = "stock-session-unknown"
