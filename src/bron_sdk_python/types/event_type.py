from enum import Enum


class EventType(Enum):
    IN = "in"
    OUT = "out"
    FEE = "fee"
    NEGATIVE_DEPOSIT = "negative-deposit"
    STAKE_DELEGATION = "stake-delegation"
    STAKE_UNDELEGATION = "stake-undelegation"
    STAKE_CLAIM = "stake-claim"
    STAKE_EARN_REWARD = "stake-earn-reward"
    STAKE_REWARD_ACCRUED = "stake-reward-accrued"
    ALLOWANCE = "allowance"
    NFT_IN = "nft-in"
    NFT_OUT = "nft-out"
    LOYALTY_LOCK = "loyalty-lock"
    LOYALTY_UNLOCK = "loyalty-unlock"
    LOYALTY_REWARD = "loyalty-reward"
