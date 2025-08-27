from enum import Enum


class TransactionStatus(Enum):
    NEW = "new"
    WAITING_CONFIRMATIONS = "waiting-confirmations"
    WAITING_APPROVAL = "waiting-approval"
    APPROVED = "approved"
    AWAITING_SECURITY_POLICY = "awaiting-security-policy"
    COMPLETED = "completed"
    CANCELED = "canceled"
    EXPIRED = "expired"
    SIGNING_REQUIRED = "signing-required"
    SIGNING = "signing"
    SIGNED = "signed"
    BROADCASTED = "broadcasted"
    MANUAL_RESOLVING = "manual-resolving"
    FAILED_ON_BLOCKCHAIN = "failed-on-blockchain"
    REMOVED_FROM_BLOCKCHAIN = "removed-from-blockchain"
    ERROR = "error"
