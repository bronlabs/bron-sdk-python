from enum import Enum


class KeyType(Enum):
    SECP256K1 = "secp256k1"
    EDWARDS25519 = "edwards25519"
    BLS12381G1 = "BLS12381G1"
    PALLAS = "pallas"
    RSA4096 = "RSA4096"
