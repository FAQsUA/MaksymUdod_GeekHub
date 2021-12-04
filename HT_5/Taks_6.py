''' 6.  Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
        P.S. Повинен вертатись генератор.
        P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range '''
class Range_Error(Exception):
    status = {0:'castom_range arg 3 must not be zero',
              1:'Error castom_range arg 2 must be greater than arg 1',
              2:'Error castom_range arg 1 must be greater than arg 2',
              3:'Error all args = 0', }

def castom_range(start=0, stop = object(), step=1):

    range_list = []

    if start == 0 and stop == 0:
        try:
            raise Range_Error()
        except Range_Error as obj:
            return print(obj.status[3])

    elif step > 0:
        
        if start >= stop:
            try:
                raise Range_Error()
            except Range_Error as obj:
                return print(obj.status[1])

        else:
            while start < stop:
                range_list.append(start)
                start += step
            print([element for element in range_list])

    elif step < 0:
        
        if start < stop :
            try:
                raise Range_Error
            except Range_Error as obj:
                return print(obj.status[2])
 
        else:
            while start > stop:
                range_list.append(start)
                start += step
            return print([element for element in range_list])
    else:
        try: 
            raise Range_Error()
        except Range_Error as obj:
            return print(obj.status[0])

castom_range(-10,100,10)

