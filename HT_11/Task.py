""" Сайт для виконання завдання: https://jsonplaceholder.typicode.com
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки """

import request_module
import menu_module


def user_id_input():
    flag = True
    while flag:
        try:
            print('*'*25)
            user_id = int(input(' Введіть id (від 1 до 10 включно) --> '))
            if user_id in range(1, 11):
                users_list = request_module.take_short_inf_request()
                flag = False
                user_id -= 1
            else:
                raise ValueError
        except ValueError:
            print('Err!!')
            continue

    print(f' id: {users_list[user_id]["id"]}\n Name : {users_list[user_id]["name"]}\n Username: {users_list[user_id]["username"]}\n', end='')
    print('*' * 25)

    return user_id + 1


def start():

    user_id = user_id_input()
    menu_module.menu(user_id)


start()
