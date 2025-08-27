# Bron SDK Python

Python SDK for Bron API
## Features

- **Complete API Coverage**: All Bron API endpoints supported
- **Async I/O**: Non-blocking HTTP using httpx
- **JWT Authentication**: Automatic ES256 JWT for requests
- **Key Generation**: Built-in JWK EC P-256 key pair generator
- **Code Generation**: Generate APIs/types from OpenAPI
- **Optional Query Parameters**: Pass only what you need

## Installation

```bash
pip install -e .
```

## Example

```python
import os, asyncio, uuid
from bron_sdk_py import BronClient
import bron_sdk_py.types as types

async def main():
	client = BronClient(
		api_key=os.environ["BRON_API_KEY"],
		workspace_id=os.environ["BRON_WORKSPACE_ID"],
	)

	# Workspace
	ws = await client.workspaces.get_workspace_by_id()
	print("your workspace:", ws)

	# Accounts
	accounts = await client.accounts.get_accounts()
	print("accounts:")
	for a in accounts.get("accounts", []):
		print(" -", a.get("accountId"), a.get("name"))
	if not accounts.get("accounts"):
		await client.aclose(); return
	account_id = accounts["accounts"][0]["accountId"]

	# Optional typed query: balances for the first account (limit 5)
	balances = await client.balances.get_balances(types.get_balances_query(accountIds=[account_id], limit="5"))
	print("balances (limit 5):")
	for b in balances.get("balances", []):
		print(" -", b.get("assetId"), b.get("symbol"), b.get("totalBalance"))

	# Send a withdrawal transaction from that account
	tx_body: types.create_transaction = {
		"accountId": account_id,
		"externalId": str(uuid.uuid4()),
		"transactionType": types.transaction_type.WITHDRAWAL.value,
		"params": {
			"amount": "0.0001",
			"assetId": "10002",
			"toAddress": "0x39695a3B42aae1Fb89De54A0cef03fbC30Aa9B80",
		},
	}
	tx = await client.transactions.create_transaction(tx_body)
	print("created tx:", tx.get("transactionId"))

	await client.aclose()

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

- Methods accept typed query objects (e.g., `get_balances_query`) or compatible dicts.

## Key Generation

CLI:
```bash
python -m bron_sdk_py.utils.key_generator
```

Programmatic:
```python
from bron_sdk_py.utils.key_generator import generate_key_pair
public_jwk, private_jwk, kid = generate_key_pair()
```

## License

MIT License - see LICENSE file for details.


