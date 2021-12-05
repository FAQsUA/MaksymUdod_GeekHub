''' 6.  Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
        P.S. Повинен вертатись генератор.
        P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range '''
class Range_Error(Exception):
    status = {0:'castom_range arg 3 must not be zero',
              1:'Error castom_range arg 2 must be greater than arg 1',
              2:'Error castom_range arg 1 must be greater than arg 2',
              3:'Error all args = 0', }

def castom_range(*args):

    arg = [item for item in args]
    
    if len(args) == 2:
        arg.append(1)
    elif len(args) == 1:
        arg.insert(0, 0)
        arg.append(1)

    if arg[0] == 0 and arg[1] == 0:
        try:
            raise Range_Error()
        except Range_Error as obj:
            return obj.status[3]

    elif arg[2] > 0:
        
        if arg[0] >= arg[1]:
            try:
                raise Range_Error()
            except Range_Error as obj:
                return obj.status[1]

        else:
            while arg[0] < arg[1]:
                yield arg[0]
                arg[0] += arg[2]

    elif arg[2] < 0:
        
        if arg[0] < arg[1] :
            try:
                raise Range_Error
            except Range_Error as obj:
                return obj.status[2]
 
        else:
            while arg[0] > arg[1]:
                yield arg[0]
                arg[0] += arg[2]
    else:
        try: 
            raise Range_Error()
        except Range_Error as obj:
            return obj.status[0]


for i in castom_range(10,19,2):
    print(i,end=' ')