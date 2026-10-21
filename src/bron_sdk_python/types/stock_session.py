from enum import Enum


class StockSession(Enum):
    REGULAR = "regular"
    PREMARKET = "premarket"
    POSTMARKET = "postmarket"
    OVERNIGHT = "overnight"
    OFFHOURS = "offhours"
    PAUSED = "paused"
    CLOSED = "closed"
