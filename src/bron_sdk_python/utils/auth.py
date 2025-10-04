import base64
import hashlib
import json
import time
from typing import Tuple

import jwt
from jwcrypto import jwk
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateNumbers, EllipticCurvePublicNumbers


def parse_jwk_ec_private_key(jwk_string: str) -> Tuple[jwk.JWK, str]:
    data = json.loads(jwk_string)
    if data.get("kty") != "EC" or data.get("crv") != "P-256":
        raise ValueError("Invalid or unsupported JWK format")
    key = jwk.JWK(**data)
    kid = data.get("kid", "")
    return key, kid


def generate_bron_jwt(*, method: str, path: str, body: str, kid: str, private_jwk: str) -> str:
    iat = int(time.time())
    exp = iat + 300
    message_string = f"{iat}{(method or '').upper()}{path or ''}{body or ''}"
    hash_hex = hashlib.sha256(message_string.encode()).hexdigest()

    header = {"alg": "ES256", "kid": kid}
    payload = {"iat": iat, "exp": exp, "method": method, "path": path, "message": hash_hex}

    # Build a cryptography EC private key from JWK components (x, y, d)
    jwk_obj = json.loads(private_jwk)
    if jwk_obj.get("kty") != "EC" or jwk_obj.get("crv") != "P-256":
        raise ValueError("Invalid or unsupported JWK format")

    def b64u(s: str) -> bytes:
        # add padding if needed
        rem = len(s) % 4
        if rem:
            s += "=" * (4 - rem)
        return base64.urlsafe_b64decode(s.encode())

    d_int = int.from_bytes(b64u(jwk_obj["d"]), byteorder="big")
    private_key = ec.derive_private_key(d_int, ec.SECP256R1())

    token = jwt.encode(payload, private_key, algorithm="ES256", headers=header)
    return token


