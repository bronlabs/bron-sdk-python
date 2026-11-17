from enum import Enum


class TransactionLimitType(Enum):
    TRANSACTIONS_VOLUME = "transactions-volume"
    TRANSACTION_AMOUNT = "transaction-amount"
    HYPERLIQUID_ORDERS_VOLUME = "hyperliquid-orders-volume"
    HYPERLIQUID_ORDER_AMOUNT = "hyperliquid-order-amount"
