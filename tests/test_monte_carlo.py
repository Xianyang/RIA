from mock import patch
# import numpy
import monte_carlo

@patch('numpy.random.normal', autospec=True, return_value = 1.1)
def test_year2_with_no_inflation(mock):
    assert monte_carlo.one_year_movement(100, -1, -1, 100, 0) == 210

@patch('numpy.random.normal', autospec=True, return_value = 1.05)
def test_year2_with_inflation(mock):
    assert monte_carlo.one_year_movement(100, -1, -1, 100, 0.02) == 200.98039215686273
