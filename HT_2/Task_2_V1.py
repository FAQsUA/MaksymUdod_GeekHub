'''2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]'''

# Standart

tuple_list = [(1,10),(2,2,20),(3,3,3,30)]
change_tuple_list = []
fake_tuple = []

print('List --> ', tuple_list)

change_element = input('Enter Number or String for change List of tuple --> ')

for i in range(0, len(tuple_list)):
    # take tuple from list
    fake_tuple = list(tuple_list[i])
    # change last element on tuple 
    fake_tuple[-1] = change_element
    # add new tuple to new list
    change_tuple_list.append(tuple(fake_tuple))

print('List  --> ', change_tuple_list)
