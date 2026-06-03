from enum import Enum


class BankChannelType(Enum):
    SEPA = "sepa"
    ACH = "ach"
    SWIFT = "swift"
    FEDWIRE = "fedwire"
    LOCAL = "local"
