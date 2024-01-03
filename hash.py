import hashlib


async def hash_sha256(origin: str, count: int = 5):
    digest = origin
    for i in range(count):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

    return digest
