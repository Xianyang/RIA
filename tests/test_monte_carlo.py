from mock import patch
# import numpy
import monte_carlo


@patch('numpy.random.normal', autospec=True, return_value = 1.1)
def test_year2_with_no_inflation(mock):
    assert monte_carlo.one_year_movement(100, -1, -1, 100, 0) == 210


@patch('numpy.random.normal', autospec=True, return_value = 1.05)
def test_year2_with_inflation(mock):
    assert monte_carlo.one_year_movement(100, -1, -1, 100, 0.02) == 200.98039215686273


@patch('monte_carlo.one_year_movement', autospec=True, return_value = -1)
def test_one_year_movement_calls(mock):
    monte_carlo.monte_carlo((40, 60, 80), 0, 0.07, 0.15, 100000, -90000, 0.02, 30)
    assert len(mock.mock_calls) == 30 * 40
