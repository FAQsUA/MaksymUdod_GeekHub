# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та 
# також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def decorator(function):
    def print_():
        print('\n'+'*'*35)
        function()
        print('*'*35 + '\n')

    return print_

def func_1():
    return 'function 1'

def func_2():
    return 'function 2'

def func_3():
    return 'function 3'

@decorator
def func():
    a = func_1()
    b = func_2()
    c = func_3()

    return print(a +' ' + b + ' ' + c)

func()