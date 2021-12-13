''' 1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" 
   деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається 
   мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму 
   (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він 
   працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти 
   номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно 
   було 100 + 20 + 20 + 20 ).

   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, 
     наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь 
    код наново (завдання на самоконтроль).
    До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
     '''

import json
import os
 
path = os.path.dirname(os.path.realpath(__file__)) + '/'

def validation():

    with open(path + "users.data", 'r', encoding='utf-8') as users_file:
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
    return str('\nВведіть дію:\n 1. Продивитись баланс\n 2. Поповнити баланс\n 3. Зняти з балансу \n 4. Історія\n 5. Вихід\n 0. Інкассація')

def menu_collection():
    return str('\nВведіть дію:\n 1. Переглянути наявні купюри\n 2. Змінити кількість купюр\n 3. Вихід')

def continue_or_exit(user):

    while True:
            operation = input('Продовжити (1) / Вихід (0) --> ')
            try:
                if int(operation) == 0:
                    print(':`( Пакєда')
                    exit()
            
                elif int(operation) == 1:
                    if user == 'admin':
                        print(menu_collection())
                        return True
                    else:
                        print(menu())
                        return True
            except ValueError:
                print('Не вірна операція!')
                continue

def view_balance(user):
    with open(path + user + "_balance.data", 'r', encoding='utf-8') as user_balance:
        print(f'Баланс {user} --> {user_balance.read()}')
    return continue_or_exit(user)
        
def deposit(user):
    while True:
        
        try:
            deposit = int(input('Введіть сумму депозиту --> '))

            if deposit < 0:
                print('Депозит не може бути відємним =)')
                continue
            else:
                with open(path + user + "_balance.data", 'r+', encoding='utf-8') as user_balance:
                    old_balance = user_balance.read()
                    new_balance = int(old_balance) + int(deposit)
                
                    user_balance.truncate(0)
                    user_balance.seek(0)
                    user_balance.write(str(new_balance))
                    user_balance.seek(0)

                    print(f'Баланс: {user_balance.read()}')
                    with open(path + user + "_transactions.data", 'a', encoding='utf-8') as user_transactions:
                        user_transactions.write(json.dumps(f"Депозит {deposit} , Баланс: {new_balance}", ensure_ascii=False)) 
                        user_transactions.write("\n")

            return continue_or_exit(user)

        except ValueError:
                print('Не допустимі символи')
                continue

def withdraw(user):
    while True:
        
        try:
            withdraw = int(input('Введіть сумму зняття --> '))

            if withdraw < 0:
                withdraw *= -1

            with open(path + user + "_balance.data", 'r+', encoding='utf-8') as user_balance:
                old_balance = user_balance.read()

                if withdraw <= int(old_balance):
                    new_balance = int(old_balance) - int(withdraw)

                    user_balance.truncate(0)
                    user_balance.seek(0)
                    user_balance.write(str(new_balance))
                    user_balance.seek(0)

                    print(f'Баланс: {user_balance.read()}')
                    with open(path + user + "_transactions.data", 'a', encoding='utf-8') as user_transactions:
                        user_transactions.write(json.dumps(f"Зняття {withdraw} , Баланс: {new_balance}", ensure_ascii=False))
                        user_transactions.write("\n")

                    pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(withdraw) 
                else:
                    print('Не достатньо когтів на балансі !')
                    continue

            return continue_or_exit(user)

        except ValueError:
            print('Не допустимі символи')
            continue

def transactions(user):
    try:
        with open(path + user + "_transactions.data", 'r' , encoding='utf-8') as user_transactions:
            print(f'Історія транзакцій {user} : \n{user_transactions.read()}')
    except FileNotFoundError:
        print('>>> Історія відсутня <<<')

    return continue_or_exit(user)

def view_collection(user):
    try:
        with open(path + "nominal.data", 'r' , encoding='utf-8') as money_nominal:
            nominal = json.loads(money_nominal.read())
            print(f'Наявні номінали:\n  10 - {nominal["10"]} шт.\n  20 - {nominal["20"]} шт.\n \
 50 - {nominal["50"]} шт.\n  100 - {nominal["100"]} шт.\n  200 - {nominal["200"]} шт.\n \
 500 - {nominal["500"]} шт.\n  1000 - {nominal["1000"]} шт.\n')

    except FileNotFoundError:
        print('>>> Історія відсутня <<<')

    return continue_or_exit(user)

def change_nominal(nominal):
    while True:
        dict_nominal = {}
                
        operation = input('Додати (+xxx) , Відняти (-xxx): ')
        try:
            with open(path + "nominal.data", 'r' , encoding='utf-8') as money_nominal:
                        dict_nominal = json.loads(money_nominal.read())

            if operation[0] == "+":
                dict_nominal[nominal] = dict_nominal[nominal] + int(operation)
                with open(path + "nominal.data", 'w' , encoding='utf-8') as money_nominal:
                    json.dump(dict_nominal, money_nominal)
                return True
            
            elif operation[0] == "-":
                if -int(operation) <= dict_nominal[nominal]:  
                    dict_nominal[nominal] =int(operation) + dict_nominal[nominal] 
                    with open(path + "nominal.data", 'w' , encoding='utf-8') as money_nominal:
                        json.dump(dict_nominal, money_nominal)
                    return True
                else:
                    print(f'Введене число більше ніж кількість курюр "{nominal}"')
                    continue
                    
        except ValueError:
            print('>>> Помилкова операція <<<')
            continue

        except FileNotFoundError:
                print('>>> Помилка Бази данних <<<')

        else:
            print('Не вірна операція!')
            continue

def pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(amount):
    dict_nominal = {}
    summa = 0
    with open(path + "nominal.data", 'r' , encoding='utf-8') as money_nominal:
        dict_nominal = json.loads(money_nominal.read())

    print(dict_nominal)

    for key, value in sorted(dict_nominal.items(), key=lambda x: -int(x[0])):
        while summa + int(key) <= amount and dict_nominal[key] > 0:
            summa += int(key)
            dict_nominal[key] -= 1
            
    print(dict_nominal)
                
    with open(path + "nominal.data", 'w' , encoding='utf-8') as money_nominal:
        json.dump(dict_nominal, money_nominal)

    return True
    
def change_menu():
    print('\nВиберіть купюру:\n1. 10\n2. 20\n3. 50\n4. 100\n5. 200\n6. 500\n7. 1000\n0. Назад')
    while True:
        operation = input('Вибір (№) --> ')
        try:
            if int(operation) == 1:
                return change_nominal("10")

            elif int(operation) == 2:
                return change_nominal('20')

            elif int(operation) == 3:
                return change_nominal('50')

            elif int(operation) == 4:
                return change_nominal('100')

            elif int(operation) == 5:
                return change_nominal('200')

            elif int(operation) == 6:
                return change_nominal('500')

            elif int(operation) == 7:
                return change_nominal('1000')

            elif int(operation) == 0:
                return True


        except FileExistsError:
            print('Не вірна операція!')
            continue
        else:
            print('Не вірна операція!')
            continue

def start():

    print('\nВас вітає Фуфло Банк\n')
    while True:
        user = validation()

        if user == "admin":
            while True:
                print(menu_collection())
                while True:
                    operation = input('Вибір (№) --> ')
                    try:
                        if int(operation) == 1:
                            if view_collection(user):
                                continue

                        elif int(operation) == 2:
                            if change_menu():
                                break

                        elif int(operation) == 3:
                            print(':`( Пакєда')
                            exit()

                    except ValueError:
                        print('Не вірна операція!')
                        continue
                    else:
                        print('Не вірна операція!')
                        continue
        else:
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
                    elif int(operation) == 0:
                        break

                except FileExistsError:
                    print('Не вірна операція!')
                    continue
                else:
                    print('Не вірна операція!')
                    continue

start()
