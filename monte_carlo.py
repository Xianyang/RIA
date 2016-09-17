import numpy as np


def one_year_movement(capital, annual_return, annual_risk, saving, inflation):
    movement = np.random.normal((1 + annual_return), annual_risk, 1)
    new_capital = (capital * movement[0] + saving) / (1 + inflation)

    return new_capital


def monte_carlo(capital, annual_return, annual_risk, saving, inflation):
    results = []
    for i in xrange(0, 3000):
        capital = 0
        for j in xrange(0, 20):
            capital = one_year_movement(capital, annual_return, annual_risk, saving, inflation)

        results.append(capital)
        print capital

monte_carlo(0, 0.07, 0.15, 100000, 0.02)
