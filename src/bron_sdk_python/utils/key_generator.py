import base64
import json
import secrets
from typing import Tuple

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization


def _b64url_no_pad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def generate_key_pair() -> Tuple[str, str, str]:
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    numbers = private_key.private_numbers()
    pub_numbers = numbers.public_numbers

    x = pub_numbers.x.to_bytes(32, byteorder="big")
    y = pub_numbers.y.to_bytes(32, byteorder="big")
    d = numbers.private_value.to_bytes(32, byteorder="big")

    kid = secrets.token_hex(12)

    public_jwk = {
        "kty": "EC",
        "crv": "P-256",
        "x": _b64url_no_pad(x),
        "y": _b64url_no_pad(y),
        "kid": kid,
    }

    private_jwk = {
        "kty": "EC",
        "crv": "P-256",
        "x": _b64url_no_pad(x),
        "y": _b64url_no_pad(y),
        "d": _b64url_no_pad(d),
        "kid": kid,
    }

    return json.dumps(public_jwk, indent=2), json.dumps(private_jwk), kid


def main() -> None:
    pub, priv, kid = generate_key_pair()
    print("\n-------------------------------------\n")
    print("✅ Public JWK (send to Bron):\n")
    print(pub)
    print("\n-------------------------------------\n")
    print("🔒 Private JWK (keep safe):\n")
    print(priv)
    print("\n-------------------------------------\n")


if __name__ == "__main__":
    main()


