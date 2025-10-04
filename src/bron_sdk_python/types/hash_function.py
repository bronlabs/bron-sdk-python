from enum import Enum


class HashFunction(Enum):
    NONE = "none"
    SHA256D = "sha256d"
    KECCAK256 = "keccak256"
    BLAKE2B256 = "blake2b256"
    SHA256 = "sha256"
    SHA512 = "sha512"
    SHA512_HALF = "sha512_half"
    SHA512_256 = "sha512_256"
    POSEIDON = "poseidon"
