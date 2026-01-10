from src.features import get_hash_bucket


# Final Build v3.0
def test_hashing_logic():
    """Requirement: Fast, isolated unit test."""
    result = get_hash_bucket("user_123")
    assert isinstance(result, int)
    assert 0 <= result < 1000