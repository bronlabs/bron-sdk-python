from enum import Enum


class signing_request_status(Enum):
    NEW = "new"
    SIGNED = "signed"
    BROADCASTED = "broadcasted"
    UNDER_RBF = "under-rbf"
    COMPLETED = "completed"
    MANUAL_RESOLVING = "manual-resolving"
    CANCELED = "canceled"
    ERROR_ON_BROADCAST = "error-on-broadcast"
    FAILED_ON_CHAIN = "failed-on-chain"
    MARKED_AS_ERROR = "marked-as-error"
