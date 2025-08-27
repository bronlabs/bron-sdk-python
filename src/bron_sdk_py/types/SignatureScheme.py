from enum import Enum


class SignatureScheme(Enum):
    ECDSA = "ecdsa"
    EDDSA = "eddsa"
    BLS = "bls"
    SCHNORR = "schnorr"
    RSA_PSS = "rsa-pss"
