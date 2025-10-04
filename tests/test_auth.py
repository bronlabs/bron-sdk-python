import json
import jwt

from bron_sdk_python.utils.auth import parse_jwk_ec_private_key, generate_bron_jwt

MOCK_JWK = {
    "kty": "EC",
    "crv": "P-256",
    "x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
    "y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
    "d": "870MB6gfuTJ4H3UnuUpxs5SwSxH2yf5K0uR49f6OzcP",
    "kid": "test-key-id",
}


def test_parse_jwk_valid():
    key, kid = parse_jwk_ec_private_key(json.dumps(MOCK_JWK))
    assert kid == "test-key-id"
    assert key is not None


def test_generate_jwt_basic():
    jwk_str = json.dumps(MOCK_JWK)
    token = generate_bron_jwt(method="GET", path="/api/v1/workspaces", body="", kid="test-key-id", private_jwk=jwk_str)
    assert isinstance(token, str)
    parts = token.split(".")
    assert len(parts) == 3

    payload = jwt.decode(token, options={"verify_signature": False})
    assert payload["method"] == "GET"
    assert payload["path"] == "/api/v1/workspaces"
    assert "message" in payload
    assert "iat" in payload and "exp" in payload
