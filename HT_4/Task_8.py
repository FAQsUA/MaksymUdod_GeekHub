''' 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: 
писок і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи 
з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2] '''

def func(my_l, my_s):
    my_s = -my_s % len(my_l)
    return my_l[my_s:] + my_l[:my_s]

def easy_check():

    while True:
        value = input()
        
        if str(value).replace('-','').isdigit():
            return int(value)

        elif value == 'exit':
            print('\n>>>>> EXIT <<<<<')
            return exit()
        
        else:
            print('\nWRONG / ',end=' ') 
            continue

print('Enter number of element in list (int) --> ', end='')
num_element = easy_check()

if num_element < 0:
    num_element *= -1

list_to_shift = list()

for element in range(num_element):
    list_to_shift.append(input(f'Enter element {element + 1} in list --> '))

print('Enter shift (int) --> ',end='')
shift = easy_check()

print(f'Shift on {shift} in {list_to_shift} ==>> ', func(list_to_shift, shift))
