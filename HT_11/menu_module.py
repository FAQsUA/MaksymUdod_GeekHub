""" 1. Повна інформація про користувача
    2. Пости: \
        - перелік постів користувача(ID та заголовок)
        - інформація про конкретний пост(ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
    3. ТУДУшка:\
        - список невиконаних задач
        - список виконаних задач
    4. Вивести URL рандомної картинки """

import request_module


def decision_main():
    while True:
        try:
            menu_des = int(input('Виберіть пункт --> '))
            if menu_des in range(1, 5):
                return menu_des
            else:
                print('Немає такого пункту !!!')
                continue
        except ValueError:
            print('Error !!!')
            continue


def decision_1_2():
    while True:
        des = decision_main()
        if des == 1:
            return 1
        elif des == 2:
            return 2
        else:
            print('Немає такого пункту !!!')
            continue


def menu(user_id):
    main_menu = ' 1. Повна інформація про користувача\n 2. Пости\n 3. ТУДУшка\n 4. Вивести URL рандомної картинки'
    posts_menu = ' 1. Перелік постів користувача (ID та заголовок)\n 2. Інформація про конкретний пост(ID, заголовок, ' \
                 'текст, кількість коментарів + перелік їхніх ID) '
    to_do_menu = ' 1. Cписок невиконаних задач\n 2. Cписок виконаних задач'

    while True:
        print(main_menu)
        decision = decision_main()
        if decision == 1:
            request_module.take_full_inf_request(user_id)

        elif decision == 2:
            print(posts_menu)
            decision_2 = decision_1_2()
            if decision_2 == 1:
                print('first')
                break
            elif decision_2 == 2:
                print('second')
                break

        elif decision == 3:
            print(to_do_menu)
            decision_2 = decision_1_2()
            if decision_2 == 1:
                print('first')
                break
            elif decision_2 == 2:
                print('second')
                break
