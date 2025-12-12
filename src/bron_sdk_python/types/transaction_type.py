from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    MULTI_WITHDRAWAL = "multi-withdrawal"
    NEGATIVE_DEPOSIT = "negative-deposit"
    AUTO_WITHDRAWAL = "auto-withdrawal"
    ALLOWANCE = "allowance"
    DEFI = "defi"
    DEFI_MESSAGE = "defi-message"
    ADDRESS_ACTIVATION = "address-activation"
    ADDRESS_CREATION = "address-creation"
    SWAP_LIFI = "swap-lifi"
    INTENTS = "intents"
    LOYALTY_LOCK = "loyalty-lock"
    LOYALTY_UNLOCK = "loyalty-unlock"
    LOYALTY_COLLECT_REWARDS = "loyalty-collect-rewards"
    CANTON_REWARD = "canton-reward"
    NFT_DEPOSIT = "nft-deposit"
    NFT_WITHDRAWAL = "nft-withdrawal"
    NFT_ALLOWANCE = "nft-allowance"
