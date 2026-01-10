# Test Force v1.5
from src.features import get_hash_bucket


def test_hashing_logic():
    """Requirement: Fast, isolated unit test. v1.4"""
    result = get_hash_bucket("user_123")
    assert isinstance(result, int)
    assert 0 <= result < 1000