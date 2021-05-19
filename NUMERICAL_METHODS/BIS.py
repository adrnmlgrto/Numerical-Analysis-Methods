# THIS IS A CODE FOR THE BISECTION METHOD
# INSTALL FIRST THE PRETTYTABLE PACKAGE IN YOUR LOCAL MACHINE
# python -m pip install -U prettytable

from prettytable import PrettyTable
from math import *

# Xn = c

tab = tab = PrettyTable(['n', 'a', 'b', 'Xn', 'ER'])
tab.float_format['a'] = '.5'
tab.float_format['b'] = '.5'
tab.float_format['Xn'] = '.5'
tab.float_format['ER'] = '.2'


def bs_iteration(a, b, fx, sc, dec):
    n = 1

    faS = fx.replace('x', 'a')
    fbS = fx.replace('x', 'b')

    fa = round(eval(faS), 5)
    fb = round(eval(fbS), 5)

    c = round((a+b)/2, dec)
    fcS = fx.replace('x', 'c')
    fc = round(eval(fcS), 5)

    er = -1

    tab.add_row([n, a, b, c, er])

    while n < sc:
        n += 1
        prev_c = c

        if (fa*fc) < 0:
            b = c
            fb = fc
        elif (fa*fc) > 0:
            a = c
            fa = fc
        elif (fa*fc) == 0:
            break

        c = round((a+b)/2, dec)
        fc = round(eval(fcS), 5)

        er = round(abs((c-prev_c)/c)*100, 2)
        tab.add_row([n, a, b, c, er])

    tab.align = 'r'
    print(tab)


interval_1 = float(input('a = '))
interval_2 = float(input('b = '))
str_funct = input('f(x) = ')
x = int(input('Until what iteration: '))
dp = int(input('Up to what decimal place: '))

bs_iteration(interval_1, interval_2, str_funct, x, dp)

input('Press ENTER key to continue...')
