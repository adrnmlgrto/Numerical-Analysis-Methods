# THIS IS A CODE FOR THE JACOBI ITERATIVE METHOD
# INSTALL FIRST THE DEPENDENCIES/PACKAGES IN YOUR LOCAL MACHINE

# EXECUTE THESE STATEMENTS IN THE CMD/TERMINAL
# python -m pip install -U prettytable

from prettytable import PrettyTable
from math import *

tab = PrettyTable(['n', 'Xn', 'ER'])
tab.float_format['Xn'] = '.4'
tab.float_format['ER'] = '.3'


def jc_iteration(x, y, z, fxx, fxy, fxz, sc, dec):
    x_disp = x
    y_disp = y
    z_disp = z

    prev_x = x
    prev_y = y
    prev_z = z

    tab.float_format['Xn'] = '.'+str(dec)
    tab.float_format['ER'] = '.3'

    n = 1

    x = round(eval(fxx), dec)
    y = round(eval(fxy), dec)
    z = round(eval(fxz), dec)

    x_disp = x
    y_disp = y
    z_disp = z

    erX = round(abs(((x-prev_x)/x)*100), 3)
    erY = round(abs(((y-prev_y)/y)*100), 3)
    erZ = round(abs(((z-prev_z)/z)*100), 3)

    tab.add_row([n, 'x'+str(n)+' = '+str(x_disp)+' | y'+str(n)+' = '+str(y_disp)+' | z'+str(n)+' = ' +
                 str(z_disp), str(erX)+'%, '+str(erY)+'%, '+str(erZ)+'%'])

    while n < sc:
        n += 1

        prev_x = x
        prev_y = y
        prev_z = z

        x = round(eval(fxx), dec)
        y = round(eval(fxy), dec)
        z = round(eval(fxz), dec)

        x_disp = x
        y_disp = y
        z_disp = z

        erX = round(abs(((x-prev_x)/x)*100), 3)
        erY = round(abs(((y-prev_y)/y)*100), 3)
        erZ = round(abs(((z-prev_z)/z)*100), 3)

        tab.add_row([n, 'x'+str(n)+' = '+str(x_disp)+' | y'+str(n)+' = '+str(y_disp)+' | z'+str(n)+' = ' +
                     str(z_disp), str(erX)+'%, '+str(erY)+'%, '+str(erZ)+'%'])

    tab.align = 'r'
    print(tab)


print('GAUSS-SEIDEL ITERATIVE METHOD')
print('(Plase take note of when entering f(x), exponentiation operator is ** and not ^)')
print('(Example: 3x²+2x+4 should be in the format: 3*x**2+2*x+4)\n')

i_guess_1 = float(input('Initial Guess (X1/x): '))
i_guess_2 = float(input('Initial Guess (X2/y): '))
i_guess_3 = float(input('Initial Guess (X3/z): '))

print('Input X1/X, X2/Y, X3/Z equations')
str_funct_1 = input('X1/X = ')
str_funct_2 = input('X2/Y = ')
str_funct_3 = input('X3/Z = ')

num_of_iterations = int(input('Until what iteration: '))
decimal_place = int(input('Up to what decimal place: '))

jc_iteration(i_guess_1, i_guess_2, i_guess_3, str_funct_1,
             str_funct_2, str_funct_3, num_of_iterations, decimal_place)

input('Press ENTER key to continue...')
