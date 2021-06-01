# THIS IS A CODE FOR THE JACOBI ITERATIVE METHOD
# INSTALL FIRST THE DEPENDENCIES/PACKAGES IN YOUR LOCAL MACHINE

# EXECUTE THESE STATEMENTS IN THE CMD/TERMINAL
# python -m pip install -U prettytable

from prettytable import PrettyTable
from math import *

tab = PrettyTable(['n', 'Xn', 'Xn_relaxed', 'ER'])
tab.float_format['Xn'] = '.4'
tab.float_format['Xn_relaxed'] = '4'
tab.float_format['ER'] = '.3'


def jc_iteration(x, y, z, rx, fxx, fxy, fxz, sc, dec):
    x_disp = x
    y_disp = y
    z_disp = z

    prev_x = x
    prev_y = y
    prev_z = z

    tab.float_format['Xn'] = '.'+str(dec)
    tab.float_format['Xn_relaxed'] = '.'+str(dec)
    tab.float_format['ER'] = '.3'

    n = 1

    x = eval(fxx)
    rx_x = (rx*x)+((1-rx)*prev_x)
    x_disp = round(x, dec)
    rx_x_disp = round(rx_x, dec)
    x = rx_x

    y = eval(fxy)
    rx_y = (rx*y)+((1-rx)*prev_y)
    y_disp = round(y, dec)
    rx_y_disp = round(rx_y, dec)
    y = rx_y

    z = eval(fxz)
    rx_z = (rx*z)+((1-rx)*prev_z)
    z_disp = round(z, dec)
    rx_z_disp = round(rx_z, dec)
    z = rx_z

    erX = round(abs(((rx_x-prev_x)/rx_x)*100), 3)
    erY = round(abs(((rx_y-prev_y)/rx_y)*100), 3)
    erZ = round(abs(((rx_z-prev_z)/rx_z)*100), 3)

    tab.add_row([n, 'x'+str(n)+' = '+str(x_disp)+' | y'+str(n)+' = '+str(y_disp)+' | z'+str(n)+' = ' +
                 str(z_disp), 'xr'+str(n)+' = '+str(rx_x_disp)+' | y'+str(n)+' = '+str(rx_y_disp)+' | z'+str(n)+' = '+str(rx_z_disp), str(erX)+'%, '+str(erY)+'%, '+str(erZ)+'%'])

    while n < sc:
        n += 1

        prev_x = rx_x
        prev_y = rx_y
        prev_z = rx_z

        x = eval(fxx)
        rx_x = (rx*x)+((1-rx)*prev_x)
        x_disp = round(x, dec)
        rx_x_disp = round(rx_x, dec)
        x = rx_x

        y = eval(fxy)
        rx_y = (rx*y)+((1-rx)*prev_y)
        y_disp = round(y, dec)
        rx_y_disp = round(rx_y, dec)
        y = rx_y

        z = eval(fxz)
        rx_z = (rx*z)+((1-rx)*prev_z)
        z_disp = round(z, dec)
        rx_z_disp = round(rx_z, dec)
        z = rx_z

        erX = round(abs(((rx_x-prev_x)/rx_x)*100), 3)
        erY = round(abs(((rx_y-prev_y)/rx_y)*100), 3)
        erZ = round(abs(((rx_z-prev_z)/rx_z)*100), 3)

        tab.add_row([n, 'x'+str(n)+' = '+str(x_disp)+' | y'+str(n)+' = '+str(y_disp)+' | z'+str(n)+' = ' +
                     str(z_disp), 'xr'+str(n)+' = '+str(rx_x_disp)+' | y'+str(n)+' = '+str(rx_y_disp)+' | z'+str(n)+' = '+str(rx_z_disp), str(erX)+'%, '+str(erY)+'%, '+str(erZ)+'%'])

    tab.align = 'r'
    print(tab)


print('GAUSS-SEIDEL ITERATIVE METHOD WITH RELAXATION')
print('(Plase take note of when entering f(x), exponentiation operator is ** and not ^)')
print('(Example: 3x²+2x+4 should be in the format: 3*x**2+2*x+4)\n')

i_guess_1 = float(input('Initial Guess (X1/x): '))
i_guess_2 = float(input('Initial Guess (X2/y): '))
i_guess_3 = float(input('Initial Guess (X3/z): '))

relax_value = float(input('Relaxation Value: '))

print('Input X1/X, X2/Y, X3/Z equations')
str_funct_1 = input('X1/X = ')
str_funct_2 = input('X2/Y = ')
str_funct_3 = input('X3/Z = ')

num_of_iterations = int(input('Until what iteration: '))
decimal_place = int(input('Up to what decimal place: '))

jc_iteration(i_guess_1, i_guess_2, i_guess_3, relax_value, str_funct_1,
             str_funct_2, str_funct_3, num_of_iterations, decimal_place)

input('Press ENTER key to continue...')
