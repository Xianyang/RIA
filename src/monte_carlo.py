import numpy as np


def one_year_movement(capital, annual_return, annual_risk, saving, inflation):
    movement = np.random.normal((1 + annual_return), annual_risk)
    new_capital = (capital * movement + saving) / (1 + inflation)

    return new_capital


def monte_carlo(ages, capital, annual_return, annual_risk, saving, withdraw, inflation, loop_count):
    results = []
    for i in xrange(0, loop_count):
        capital = 0
        for j in xrange(0, ages[1] - ages[0]):
            capital = one_year_movement(capital, annual_return, annual_risk, saving, inflation)

        for k in xrange(0, ages[2] - ages[1]):
            capital = one_year_movement(capital, annual_return, annual_risk, withdraw, inflation)

        results.append(capital)
        print capital

monte_carlo((40, 60, 80), 0, 0.07, 0.15, 100000, -90000, 0.02, 3000)
