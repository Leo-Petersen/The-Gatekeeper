import pytest
from src.main import conversion, is_strong, fahrenheit_to_celsius

def test_conversion():
    # 100C should be 212F
    assert conversion(100) == 212
    # 0C should be 32F
    assert conversion(0) == 32

def test_logic():
    # Average of [40, 40, 60] is 46.6 (Should be False)
    # Carl's code returns True because 60 > 50.
    data = [40, 40, 60]
    assert is_strong(data) is False

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(32) == 0