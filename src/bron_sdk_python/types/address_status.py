from enum import Enum


class AddressStatus(Enum):
    NEW = "new"
    PENDING = "pending"
    ADDRESS_ACTIVATION_REQUIRED = "address-activation-required"
    ADDRESS_CREATION_REQUIRED = "address-creation-required"
    ADDRESS_ACTIVATION_IN_PROGRESS = "address-activation-in-progress"
    APPROVAL_PENDING = "approval-pending"
    ENABLED = "enabled"
    DISABLED = "disabled"
    ERROR = "error"
    ACCOUNT_ARCHIVED = "account-archived"
