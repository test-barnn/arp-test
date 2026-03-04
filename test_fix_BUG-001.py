import pytest
from utils import calculate_discount

def test_calculate_discount_invalid_rate_high():
    """Test that ValueError is raised when rate > 1"""
    with pytest.raises(ValueError):
        calculate_discount(price=100, rate=1.15)

def test_calculate_discount_invalid_rate_negative():
    """Test that ValueError is raised when rate < 0"""
    with pytest.raises(ValueError):
        calculate_discount(price=100, rate=-0.1)

def test_calculate_discount_valid_rate():
    """Test that correct discount is returned when 0 <= rate <= 1"""
    result = calculate_discount(price=100, rate=0.15)
    assert result == 15.0

def test_calculate_discount_zero_rate():
    """Test that zero rate returns zero discount"""
    result = calculate_discount(price=100, rate=0)
    assert result == 0.0

def test_calculate_discount_one_rate():
    """Test that rate of 1 returns full price discount"""
    result = calculate_discount(price=100, rate=1)
    assert result == 100.0