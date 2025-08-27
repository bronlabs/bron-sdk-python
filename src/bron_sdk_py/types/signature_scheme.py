from enum import Enum


class signature_scheme(Enum):
    ECDSA = "ecdsa"
    EDDSA = "eddsa"
    BLS = "bls"
    SCHNORR = "schnorr"
    RSA_PSS = "rsa-pss"
