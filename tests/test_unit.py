from src.features import get_hash_bucket


def test_hashing_logic():
    """Requirement: Fast, isolated unit test. v3.1"""
    result = get_hash_bucket("user_123")
    assert isinstance(result, int)
