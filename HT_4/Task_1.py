# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

from math import sqrt

def func_square(side):
    P = 4 * side
    S = side**2
    D = sqrt(2) * side

    return print('P = ' + str(P) + '\nS = ' + str(S) + '\nD = ' + str(D))

while True:
    side_a = input('Enter sdie square (cm) --> ')

    if side_a.replace('.','').isdigit():
        try:
            func_square(float(side_a))
            continue
        except:
            print('WRONG / Enter digit')
            continue
    elif side_a == 'exit':
        print('>>>>> EXIT <<<<<')
        break
    else:
        print('WRONG / Enter digit')
        continue
