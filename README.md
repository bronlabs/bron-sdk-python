# Bron SDK Python

Python SDK for Bron API

## Features

- **Complete API Coverage**: All Bron API endpoints supported
- **Async I/O**: Non-blocking HTTP using httpx
- **JWT Authentication**: Automatic ES256 JWT for requests
- **Typed Queries**: Typed query objects for all API endpoints

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Example

```python
import asyncio
import os
import uuid

from bron_sdk_python import BronClient
from bron_sdk_python.types.create_transaction import CreateTransaction
from bron_sdk_python.types.transaction_type import TransactionType


async def main() -> None:
    client = BronClient(
        api_key=os.environ["BRON_API_KEY"],
        workspace_id=os.environ["BRON_WORKSPACE_ID"],
    )

    ws = await client.workspaces.get_workspace_by_id()
    print(f"your workspace: {ws}")

    accounts = await client.accounts.get_accounts()
    print("accounts:")
    for a in accounts.get("accounts", []):
        print(f" - {a.get('accountId')} {a.get('accountName')}")
    if not accounts.get("accounts"):
        await client.aclose()
        return

    account_id = accounts["accounts"][0]["accountId"]

    balances = await client.balances.get_balances({"accountIds": [account_id], "limit": 5})
    print("balances (limit 5):")
    for b in balances.get("balances", []):
        print(f" - {b.get('assetId')} {b.get('symbol')} {b.get('totalBalance')}")

    tx_body: CreateTransaction = {
        "accountId": account_id,
        "externalId": str(uuid.uuid4()),
        "transactionType": TransactionType.WITHDRAWAL.value,
        "params": {
            "amount": "0.0001",
            "assetId": "10002",
            "toAddress": "0x39695a3B42aae1Fb89De54A0cef03fbC30Aa9B80",
        },
    }
    tx = await client.transactions.create_transaction(tx_body)
    print(f"created tx: {tx.get('transactionId')}")

    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())
```

## Async requirement

All public API methods are async. Use `await` (or `asyncio.run(...)`). Close with `await client.aclose()`.

## Configuration

- `api_key`: Your private JWK (required)
- `workspace_id`: Your workspace ID (required)
- `base_url`: API base URL (defaults to https://api.bron.org)

## Authentication

The SDK generates an ES256 JWT per request from your private JWK and sends it in `Authorization: ApiKey <jwt>`.

## Query Parameters

Methods accept typed query objects or compatible dicts.

## Key Generation

CLI:

```bash
python -m bron_sdk_python.utils.key_generator
```

Programmatic:

```python
from bron_sdk_python.utils.key_generator import generate_key_pair

public_jwk, private_jwk, kid = generate_key_pair()
```

## License

MIT License - see LICENSE file for details.


