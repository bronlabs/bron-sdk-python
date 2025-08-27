# Bron SDK Python

Python SDK for the Bron API. Mirrors the structure/behavior of the Go and TypeScript SDKs.

## Features

- **Complete API Coverage**: All Bron API endpoints supported
- **Async I/O**: Non-blocking HTTP using httpx
- **JWT Authentication**: Automatic ES256 JWT for requests
- **Key Generation**: Built-in JWK EC P-256 key pair generator
- **Code Generation**: Generate APIs/types from OpenAPI
- **Optional Query Parameters**: Pass only what you need

## Install

```bash
pip install -e .
```

## Generate API Keys

```bash
python -m bron_sdk_py.utils.key_generator
```

This prints:
- Public JWK (send to Bron)
- Private JWK (keep safe; use as BRON_API_KEY)

## Usage Example (async)

Set env vars:

```bash
export BRON_API_KEY='{"kty":"EC","x":"...","y":"...","crv":"P-256","d":"...","kid":"..."}'
export BRON_WORKSPACE_ID='your_workspace_id'
# optional; if empty or unset defaults to https://api.bron.org
export BRON_BASE_URL='' 
```

Example script:

```python
import os, asyncio
from uuid import uuid4
from bron_sdk_py import BronClient

async def main():
	client = BronClient(
		api_key=os.environ["BRON_API_KEY"],
		workspace_id=os.environ["BRON_WORKSPACE_ID"],
		base_url=os.getenv("BRON_BASE_URL", "https://api.bron.org"),
	)

	workspace = await client.workspaces.getWorkspaceById()
	print("Workspace:", workspace.get("name"))

	accounts = await client.accounts.getAccounts()
	if accounts["accounts"]:
		account = accounts["accounts"][0]
		balances = await client.balances.getBalances({
			"accountIds": [account["accountId"]]
		})
		for b in balances["balances"]:
			print("Balance", b.get("assetId"), b.get("symbol"), b.get("totalBalance"))

		tx = await client.transactions.createTransaction({
			"accountId": account["accountId"],
			"externalId": str(uuid4()),
			"transactionType": "withdrawal",
			"params": {
				"amount": "0.001",
				"symbol": "ETH",
				"networkId": "testETH",
				"toAddress": "0x428CdE5631142916F295d7bb2DA9d1b5f49F0eF9"
			}
		})
		print("Created tx:", tx.get("transactionId"))

	await client.aclose()

asyncio.run(main())
```

## Configuration

- `api_key`: Private JWK string (required)
- `workspace_id`: Workspace ID (required)
- `base_url`: API base (default: https://api.bron.org; empty/whitespace coerced to default)

## Authentication

The SDK generates an ES256 JWT per request from your private JWK and sends it in `Authorization: ApiKey <jwt>`.

## Error Handling

Wrap calls in try/except to handle HTTP or validation errors.


