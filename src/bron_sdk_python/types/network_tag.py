from enum import Enum


class NetworkTag(Enum):
    SHOW_VAULT = "show-vault"
    SUPPORTS_RBF = "supports-rbf"
    SUPPORTS_RBF_CANCEL = "supports-rbf-cancel"
    SUPPORTS_MEMO = "supports-memo"
    SWAP = "swap"
    SUPPORTS_PARALLEL_SIGNING = "supports-parallel-signing"
    SUPPORTS_CHAINED_SIGNING = "supports-chained-signing"
    SUPPORTS_FEE_LEVELS = "supports-fee-levels"
