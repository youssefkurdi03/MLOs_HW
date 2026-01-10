import pytest
from src.features import get_hash_bucket

def test_get_hash_bucket_integration():
    """
    Component Test: Verifies the feature logic is accessible 
    and returns expected data types.
    """
    sample_input = "mlops_user_test"
    result = get_hash_bucket(sample_input)
    
    assert isinstance(result, int)
    assert 0 <= result < 1000