from mock import patch
import numpy
import monte_carlo


@patch('numpy.random.normal', autospec=True, side_effect = numpy.arange(1.01, 1.13, 0.0001))
def test_monte_carlo_results(mock):
    result = monte_carlo.monte_carlo((40, 60, 80), 0, 0.07, 0.15, 100000, -90000, 0.02, 30)
    assert result == [-83445.627765943005, 47146.842719978304,
            198455.99841999955, 373253.44904969464, 574663.70538707403,
            806208.06985985255, 1071853.8905247787, 1376069.8221526896,
            1723887.8138270322, 2120972.6268520122, 2573699.7808221048,
            3089242.9305055141, 3675671.7929354459, 4342061.8741089925,
            5098617.3894305322, 5956808.9331290079, 6929527.6311243139,
            8031257.7112062583, 9278269.6461226791, 10688836.271683738,
            12283474.555971773, 14085216.00017295, 16119908.989708012,
            18416556.789867241, 21007695.29705821, 23929815.119485822,
            27223833.074489076, 30935618.759251505, 35116582.483132496,
            39824331.549998134]


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
