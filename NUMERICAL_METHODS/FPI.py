# THIS IS A CODE FOR THE FIXED POINT ITERATION METHOD
# INSTALL FIRST THE PRETTYTABLE PACKAGE IN YOUR LOCAL MACHINE
# python -m pip install -U prettytable

from prettytable import PrettyTable
from math import *

tab = PrettyTable(['n', 'Xn', 'Xn+1', 'ER'])
tab.float_format['Xn'] = '.4'
tab.float_format['Xn+1'] = '.4'
tab.float_format['ER'] = '.2'


def fp_iteration_ER(x, fx, sc, dec):
    # x = Xn
    # fx = the isolated x value
    # sc = stopping criterion

    tab.float_format['Xn'] = '.'+str(dec)
    tab.float_format['Xn+1'] = '.'+str(dec)

    n = 0
    y = round(eval(fx), dec)  # Xn+1
    er = round(abs((y-x)/y*100), 2)

    tab.add_row([n, x, y, er])

    if er <= sc:
        return

    while 1:
        if er <= 20:
            break
        else:
            n += 1
            x = y
            y = round(eval(fx), dec)
            er = round(abs((y-x)/y*100), 2)
            tab.add_row([n, x, y, er])

    tab.align = 'r'
    print(tab)


def fp_iteration_IT(x, fx, sc, dec):
    # x = Xn
    # fx = the isolated x value
    # sc = stopping criterion

    tab.del_column('ER')
    tab.float_format['Xn'] = '.'+str(dec)
    tab.float_format['Xn+1'] = '.'+str(dec)

    n = 0
    y = round(eval(fx), dec)  # Xn+1

    tab.add_row([n, x, y])

    while n < sc:
        n += 1
        x = y
        y = round(eval(fx), dec)
        tab.add_row([n, x, y])

    tab.align = 'r'
    print(tab)


i_root = int(input('X0: '))
str_funct = input('X = ')

print('Stopping Criterion: [1] Until %ER(x%), [2] Until xth Iteration')
choice = int(input('Enter choice: '))

if choice == 1:

    x = float(input('Until what percent: '))
    dp = int(input('Up to what decimal place: '))
    fp_iteration_ER(i_root, str_funct, x, dp)

    input('Press ENTER key to continue...')

elif choice == 2:

    x = int(input('Until what iteration: '))
    dp = int(input('Up to what decimal place: '))
    fp_iteration_IT(i_root, str_funct, x, dp)

    input('Press ENTER key to continue...')

else:
    print('Invalid Choice. Ending program.')
    input('Press ENTER key to continue...')
