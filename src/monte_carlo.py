import numpy as np
import plotly
import plotly.graph_objs as go

_annual_return = 0.07
_annual_risk = 0.15
_capital = 0
_inflation = 0.02
_ages = [40, 60]
_annual_saving = 100000
_annual_withdraw = -90000
_expect_age = 85

_loop_count = 1000


def one_year_movement(capital, annual_return, annual_risk, saving, inflation):
    movement = np.random.normal((1 + annual_return), annual_risk)
    new_capital = (capital * movement + saving) / (1 + inflation)

    return new_capital


def monte_carlo(annual_return, annual_risk, capital, inflation, ages, annual_saving, annual_withdraw, expect_age, loop_count):
    capital_list = []
    annual_capital_list = []
    for i in xrange(0, loop_count):
        new_capital = capital
        annual_capital = []
        for j in xrange(0, ages[1] - ages[0]):
            new_capital = one_year_movement(new_capital, annual_return, annual_risk, annual_saving, inflation)
            annual_capital.append(new_capital)

        for k in xrange(0, expect_age - ages[1]):
            new_capital = one_year_movement(new_capital, annual_return, annual_risk, annual_withdraw, inflation)
            annual_capital.append(new_capital)

        annual_capital_list.append(annual_capital)
        capital_list.append(new_capital)
        print new_capital

    return capital_list, annual_capital_list


def add_line_extension(figure, xData, yData, name, dashStyle, color):
    extension = go.Scatter(
        x=xData,
        y=yData,
        mode='lines',
        name=name,
        line=dict(
            color=color,
            dash=dashStyle
        )
    )

    figure['data'].extend([extension])


if __name__ == '__main__':
    print 'start monte carlo'

    # read parameters from database
    # this program need 9 parameters
    # annual_return, annual_risk, capital, inflation, ages, annual_saving, retire_age, annual_withdraw, expect_age

    # step 1: run the monte carlo algorithm
    capital_list, annual_capital_list = monte_carlo(_annual_return, _annual_risk, _capital, _inflation,
                                                    _ages, _annual_saving, _annual_withdraw, _expect_age, _loop_count)
    print 'average is %f' % np.mean(capital_list)
    print 'std is %f' % np.std(capital_list)

    # step 2: draw the chart
    age_list = []
    start_age = _ages[0]
    for age in range(start_age, _expect_age, 1):
        age_list.append(age)


    data_to_figure = []
    for annual_capital in annual_capital_list:
        trace = go.Scatter(
            x=age_list,
            y=annual_capital,
            mode='lines',
            name='lines'
        )

        data_to_figure.append(trace)

    layout = dict(title='Capital',
                  xaxis=dict(title='Age'),
                  yaxis=dict(title='Capital'),
                  )

    fig = dict(data=data_to_figure, layout=layout)

    plotly.offline.plot(fig, filename='file.html')

    # plotly.plotly.image.save_as(fig, 'data.png')

