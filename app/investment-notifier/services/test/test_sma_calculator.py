from services.sma_calculator import calculate_rate_of_change


def test_sma_calculator_with_positive_change():
    result = calculate_rate_of_change([100, 100, 99, 96, 90, 95])
    assert result == 2.0


def test_sma_calculator_with_negative_change():
    result = calculate_rate_of_change([50, 60, 70, 80, 77])
    assert result == -15.0


def test_sma_calculator_at_boundary():
    result = calculate_rate_of_change([100, 100, 99, 96, 90, 70])
    assert result == 5.0
