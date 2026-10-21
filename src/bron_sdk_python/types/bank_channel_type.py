from enum import Enum


class BankChannelType(Enum):
    SEPA = "sepa"
    ACH = "ach"
    SWIFT = "swift"
    FEDWIRE = "fedwire"
    FEDNOW = "fednow"
    LOCAL = "local"
