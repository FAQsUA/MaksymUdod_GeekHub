''' 5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
    пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при 
    нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z '''

def function_(x, y):
    
    if x > y:
        z = x - y
        print('X бiльше нiж Y на ', z)
    elif x < y:
        z = y - x
        print('Y бiльше нiж X на ', z)
    elif x == y:
       print('X дорiвнює Y')

x, y = int(input('X(digit) = ')), int(input('Y(digit) = '))

function_(x, y)