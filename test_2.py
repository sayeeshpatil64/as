from celsius import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    result = celsius_to_fahrenheit(25)
    expected = 77.0
    assert result == expected
