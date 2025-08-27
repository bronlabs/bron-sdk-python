from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    MULTI_WITHDRAWAL = "multi-withdrawal"
    NEGATIVE_DEPOSIT = "negative-deposit"
    AUTO_WITHDRAWAL = "auto-withdrawal"
    ALLOWANCE = "allowance"
    RAW_TRANSACTION = "raw-transaction"
    ADDRESS_ACTIVATION = "address-activation"
    ADDRESS_CREATION = "address-creation"
    SWAP_LIFI = "swap-lifi"
    INTENTS = "intents"
