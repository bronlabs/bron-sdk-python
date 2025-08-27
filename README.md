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

async def main():
	client = BronClient(
		api_key=os.environ["BRON_API_KEY"],
		workspace_id=os.environ["BRON_WORKSPACE_ID"],
	)

	ws = await client.workspaces.getWorkspaceById()
	print(ws)

	await client.accounts.getAccounts()

	account_id = "nlvl2t3azfeszd04jsar4fa8"
	to = "0x39695a3B42aae1Fb89De54A0cef03fbC30Aa9B80"
	asset_id = "10002"

	tx = await client.transactions.createTransaction({
		"accountId": account_id,
		"externalId": str(uuid.uuid4()),
		"transactionType": "withdrawal",
		"params": {
			"amount": "0.0001",
			"assetId": asset_id,
			"toAddress": to,
		},
	})
	print("Created tx", tx.get("transactionId"))

	await client.aclose()

asyncio.run(main())
```

**Get Accounts & Balances:**

```python
import asyncio, os
from bron_sdk_py import BronClient

async def main():
	client = BronClient(api_key=os.environ["BRON_API_KEY"], workspace_id=os.environ["BRON_WORKSPACE_ID"]) 

	accounts = await client.accounts.getAccounts()
	balances = await client.balances.getBalances()

	if accounts["accounts"]:
		account = accounts["accounts"][0]
		filtered = await client.balances.getBalances({"accountIds": [account["accountId"]]})
		for b in filtered["balances"]:
			print("Balance", b.get("assetId"), b.get("symbol"), b.get("totalBalance"))

	await client.aclose()

asyncio.run(main())
```

**More Examples:**

```python
# Get transactions
transactions = await client.transactions.getTransactions()

# Filtered transactions
recent = await client.transactions.getTransactions({"limit": "10"})

# Assets / Dictionaries
assets = await client.assets.getAssets()

# Address book record
record = await client.addressBook.createAddressBookRecord({
	"name": "My Address",
	"address": "0x428CdE5631142916F295d7bb2DA9d1b5f49F0eF9",
	"networkId": "testETH",
})
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

- Call without parameters: `await client.accounts.getAccounts()`
- Or pass a dict: `await client.accounts.getAccounts({"limit": "10"})`

## Return Types

API methods return JSON-like Python dicts.

## Error Handling

```python
try:
	ws = await client.workspaces.getWorkspaceById()
except Exception as e:
	print("API error:", e)
```

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


