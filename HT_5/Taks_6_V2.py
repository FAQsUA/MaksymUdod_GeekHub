''' 6.  Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
        P.S. Повинен вертатись генератор.
        P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range '''

def castom_range(start, stop, step = 1):
    range_list = []

    while start < stop:
        
        range_list.append(start)
        start += step

    return [element for element in range_list]

print(castom_range(0,9))