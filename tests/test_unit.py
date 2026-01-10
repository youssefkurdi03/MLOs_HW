def test_hashing_logic():
    """Requirement: Fast, isolated test with no external dependencies."""
    input_str = "user_123"
    result = hash(input_str) % 1000
    assert isinstance(result, int)
    assert 0 <= result < 1000
