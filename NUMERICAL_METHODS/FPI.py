# THIS IS A CODE FOR THE FIXED POINT ITERATION METHOD
from prettytable import PrettyTable
from math import sin, cos, tan

e = 2.71828

tab = PrettyTable()


def fp_iteration_ER(x, fx, sc):
    # x = Xn
    # fx = the isolated x value
    # sc = stopping criterion

    tab.field_names = ['n', 'Xn', 'Xn+1', 'ER']

    n = 0
    y = round(eval(fx), 4)  # Xn+1
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
            y = round(eval(fx), 4)
            er = round(abs((y-x)/y*100), 2)
            tab.add_row([n, x, y, er])

    print(tab)


def fp_iteration_IT(x, fx, sc, dec):
    # x = Xn
    # fx = the isolated x value
    # sc = stopping criterion

    tab.field_names = ['n', 'Xn', 'Xn+1']

    n = 0
    y = round(eval(fx), dec)  # Xn+1

    tab.add_row([n, x, y])

    while n < sc:
        n += 1
        x = y
        y = round(eval(fx), dec)
        tab.add_row([n, x, y])

    print(tab)


i_root = int(input('X0: '))
str_funct = input('X = ')

print('Stopping Criterion: [1] Until %ER(x%), [2] Until xth Iteration%s')
choice = int(input('Enter choice: '))

if choice == 1:

    x = float(input('Until what percent: '))
    fp_iteration_ER(i_root, str_funct, x)

elif choice == 2:
    x = int(input('Until what iteration: '))
    dp = int(input('Up to what decimal place: '))
    fp_iteration_IT(i_root, str_funct, x, dp)
else:
    print('Invalid Choice. Ending program.')
