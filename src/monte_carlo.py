import numpy as np
import plotly
import plotly.graph_objs as go

_annual_return = 0.07
_annual_risk = 0.15
_capital = 0
_inflation = 0.03
_ages = [40, 60]
_annual_saving = 12000
_annual_withdraw = -60000
_expect_age = 85

_loop_count = 1000


def one_year_movement(capital, annual_return, annual_risk, saving, inflation):
    movement = np.random.normal((1 + annual_return), annual_risk)
    new_capital = (capital * movement + saving) / (1 + inflation)

    return new_capital


def monte_carlo(annual_return, annual_risk, capital, inflation, ages, annual_saving, annual_withdraw, expect_age, loop_count):
    capital_list = []
    annual_capital_list = []
    fail_count = 0.0
    for i in xrange(0, loop_count):
        new_capital = capital
        annual_capital = []
        for j in xrange(0, ages[1] - ages[0]):
            new_capital = one_year_movement(new_capital, annual_return, annual_risk, annual_saving, inflation)
            annual_capital.append(new_capital)

        for k in xrange(0, expect_age - ages[1]):
            new_capital = one_year_movement(new_capital, annual_return, annual_risk, annual_withdraw, inflation)
            annual_capital.append(new_capital)

        if new_capital < 0:
            fail_count += 1

        annual_capital_list.append(annual_capital)
        capital_list.append(new_capital)
        # print new_capital

    return capital_list, annual_capital_list, fail_count / loop_count


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
    capital_list, annual_capital_list, depletion_rate = monte_carlo(_annual_return, _annual_risk, _capital, _inflation,
                                                    _ages, _annual_saving, _annual_withdraw, _expect_age, _loop_count)
    print 'average is %f' % np.mean(capital_list)
    print 'std is %f' % np.std(capital_list)
    print 'depletion rate is %f' % depletion_rate

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
            name=''
        )

        data_to_figure.append(trace)

    # get median number
    sorted_capital_list = sorted(capital_list)
    median = sorted_capital_list[_loop_count / 2]
    median_index = capital_list.index(median)
    trace = go.Scatter(
        x=age_list,
        y=annual_capital_list[median_index],
        mode='lines',
        line=dict(
            color='yellow',
            width=5
        )
    )
    data_to_figure.append(trace)

    # add retirement age
    trace = go.Scatter(
        x=[_ages[1], _ages[1]],
        y=[-3000000, 3000000],
        mode='line',
        name=''
    )
    data_to_figure.append(trace)

    # add 0 line
    trace = go.Scatter(
        x=[_ages[1], _expect_age - 2],
        y=[0, 0],
        mode='line',
        line=dict(
            color='white',
            width=3
        )
    )

    data_to_figure.append(trace)

    titie = 'Monte Carlo Result - depletion rate %.3f' % (depletion_rate * 100) + '%'
    layout = dict(title=titie,
                  xaxis=dict(title='Age'),
                  yaxis=dict(title='Capital'),
                  )

    fig = dict(data=data_to_figure, layout=layout)

    plotly.offline.plot(fig, filename='monte_carlo.html')

    # plotly.plotly.image.save_as(fig, 'data.png')

