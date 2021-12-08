''' 1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :) '''

import json
from pathlib import Path
 
def validation():

    with open(Path("Task_1","users.data"), 'r', encoding='utf-8') as users_file:
        users = json.loads(users_file.read())

        while True:
            login = str(input('Введіть логін --> '))
            if login in users:
                while True:
                    password = str(input('Введіть пароль -->'))
                    if password == users[login]:
                        return login
                    else:
                        print('Не вірний пароль (((')
                        continue
            else:
                print('Не вірний логін (((')
                continue

def menu():
    return str('\nВведіть дію:\n 1. Продивитись баланс\n 2. Поповнити баланс\n 3. Зняти з балансу \n 4. Історія\n 5. Вихід')

def continue_or_exit():
    #menu = '\nВведіть дію:\n 1. Продивитись баланс\n 2. Поповнити баланс\n 3. Зняти з балансу\n 4. Вихід \n'
    while True:
            operation = input('Продовжити (1) / Вихід (0) --> ')
            try:
                if int(operation) == 0:
                    print(':`( Пакєда')
                    exit()
            
                elif int(operation) == 1:
                    print(menu())
                    return True
            except ValueError:
                print('Не вірна операція!')
                continue

def view_balance(user):
    with open(Path("Task_1", user +"_balance.data"), 'r', encoding='utf-8') as user_balance:
        print(f'Баланс {user} --> {user_balance.read()}')

        return continue_or_exit()
        
def deposit(user):
    while True:
        
        try:
            deposit = int(input('Введіть сумму депозиту --> '))

            if deposit < 0:
                print('Депозит не може бути відємним =)')
                continue
            else:
                with open(Path("Task_1", user +"_balance.data"), 'r+', encoding='utf-8') as user_balance:
                    old_balance = user_balance.read()
                    new_balance = int(old_balance) + int(deposit)

                    user_balance.truncate(0)
                    user_balance.seek(0)
                    user_balance.write(str(new_balance))
                    user_balance.seek(0)

                    print(f'Баланс: {user_balance.read()}')
                    with open(Path("Task_1", user + "_transactions.data"), 'a', encoding='utf-8') as user_transactions:
                        user_transactions.write(json.dumps(f"Депозит {deposit} , Баланс: {new_balance}", ensure_ascii=False)) 
                        user_transactions.write("\n")

            return continue_or_exit()

        except ValueError:
                print('Не допустимі символи')
                continue

def withdraw(user):
    while True:
        
        try:
            withdraw = int(input('Введіть сумму зняття --> '))

            if withdraw < 0:
                withdraw *= -1

            with open(Path("Task_1", user +"_balance.data"), 'r+', encoding='utf-8') as user_balance:
                old_balance = user_balance.read()

                if withdraw <= int(old_balance):
                    new_balance = int(old_balance) - int(withdraw)

                    user_balance.truncate(0)
                    user_balance.seek(0)
                    user_balance.write(str(new_balance))
                    user_balance.seek(0)

                    print(f'Баланс: {user_balance.read()}')
                    with open(Path("Task_1", user + "_transactions.data"), 'a', encoding='utf-8') as user_transactions:
                        user_transactions.write(json.dumps(f"Зняття {withdraw} , Баланс: {new_balance}", ensure_ascii=False))
                        user_transactions.write("\n")
                        
                else:
                    print('Не достатньо когтів на балансі !')
                    continue

            return continue_or_exit()

        except ValueError:
            print('Не допустимі символи')
            continue

def transactions(user):
    try:
        with open(Path("Task_1", user + "_transactions.data"), 'r' , encoding='utf-8') as user_transactions:
            print(f'Історія транзакцій {user} : \n{user_transactions.read()}')
    except FileNotFoundError:
        print('>>> Історія відсутня <<<')

    return continue_or_exit()

def start():

    print('\nВас вітає Фуфло Банк\n')
    user = validation()

    if user:
        print(menu())
        while True:
            operation = input('Вибір (№) --> ')
            try:
                if int(operation) == 1:
                    if view_balance(user):
                        continue

                elif int(operation) == 2:
                    if deposit(user):
                        continue

                elif int(operation) == 3:
                    if withdraw(user):
                        continue
                
                elif int(operation) == 4:
                    if transactions(user):
                        continue

                elif int(operation) == 5:
                    print(':`( Пакєда')
                    exit()

            except ValueError:
                print('Не вірна операція!')
                continue
            else:
                print('Не вірна операція!')
                continue

start()
