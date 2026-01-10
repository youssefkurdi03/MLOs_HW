import hashlib


# Final Build v3.0
def get_hash_bucket(input_string, num_buckets=1000):
    """
    Hashes an input string into a fixed number of buckets.
    """
    if not input_string:
        return 0
    hash_value = hashlib.md5(str(input_string).encode()).hexdigest()
    return int(hash_value, 16) % num_buckets