''' Перепишіть програму-банкомат на використання бази даних для збереження всих даних.
Використовувати БД sqlite3 та натівний Python.
Дока з прикладами: https://docs.python.org/3/library/sqlite3.html
Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/
Для уніфікації перевірки, в базі повинні бути 3 користувача:
  ім'я: user1, пароль: user1
  ім'я: user2, пароль: user2
  ім'я: admin, пароль: admin (у цього коритувача - права інкасатора) '''

import sqlite3
import os
from sqlite3.dbapi2 import Error, connect

db_path = os.path.dirname(os.path.realpath(__file__)) + '/'
db_file = 'atm.db'


#########>>>DATABASE CONFIGURATION START<<<#########################################################################
def connection(db_file):
    if os.path.isfile(db_path+db_file):
        pass
    else:
        con = None
        try:
            con = sqlite3.connect(db_file)
            return con
        except Error as err:
            print(err)
        
        return con

def create_table(con, ct_sql):
    try:
        c = con.cursor()
        c.execute(ct_sql)
    except Error as e:
        print(e)

def ins_in_tab_users(con, sql_usr):

    try:
        sql ='''INSERT or IGNORE INTO users(id,login,pwd,flag) 
                            VALUES(?,?,?,?)'''
        c = con.cursor()
        c.execute(sql, sql_usr)
        con.commit()
        return c.lastrowid
    except Error as err:
        print(err)

def ins_in_tab_balance(con, sql_bal):
    try:
        sql = '''INSERT or IGNORE INTO balance(id,login_id,balance) 
                        VALUES(?,?,?)'''
        c = con.cursor()
        c.execute(sql, sql_bal)
        con.commit()
        return c.lastrowid
    except Error as err:
        print(err)

def ins_in_tab_nominals(con, sql_nom):
    try:
        sql = '''INSERT or IGNORE INTO nominals (id,nominal) 
                        VALUES(?,?)'''
        c = con.cursor()
        c.execute(sql, sql_nom)
        con.commit()
    except Error as err:
        print(err)

def create_db():
    db = db_path+db_file
    con = connection(db)
    
    sql_c_tab_usr = """CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        login text NOT NULL,
                                        pwd text NOT NULL,
                                        flag text NOT NULL );"""

    sql_c_tab_bal = """CREATE TABLE IF NOT EXISTS balance (
                                    id integer PRIMARY KEY,
                                    login_id integer NOT NULL,
                                    balance integer NOT NULL,
                                    FOREIGN KEY (login_id) REFERENCES users (login));"""
    sql_c_tab_nom = """CREATE TABLE IF NOT EXISTS nominals (
                            id integer PRIMARY KEY,
                            nominal integer NOT NULL );"""

    if con is not None:
        create_table(con, sql_c_tab_usr)
        create_table(con, sql_c_tab_bal)
        create_table(con, sql_c_tab_nom)
    else:
        print("Error! cannot create the database connection.")

    with con:
        for i in range(1,4):
            if i == 3:
                user = (i,'admin','admin',"True")
                login_id = ins_in_tab_users(con,user)
                break

            user = (i,'user'+str(i),'user'+str(i),"False")
            login_id = ins_in_tab_users(con,user)
            balance = (i,login_id,i*1000)
            ins_in_tab_balance(con,balance)

        nominals = [10,20,50,100,200,500,1000]
        for item in nominals:
            nominal = (item,10)
            ins_in_tab_nominals(con,nominal)

create_db()
#########>>>DATABASE CONFIGURATION END<<<#########################################################################

class NoMoney(Exception):
    pass
class NoNominal(Exception):
    pass

def validation():
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()
    
    while True:
        try:
            with con:
                login = str(input('Введіть логін --> '))
                [res_login], = c.execute("""SELECT login FROM users WHERE login=?""", (login,))
                [res_pwd], = c.execute("""SELECT pwd FROM users WHERE login=?""", (login,))
                pwd = str(input('Введіть пароль -->'))

                if pwd == res_pwd:
                    print(f'\nКористувач: {res_login}\n' + '*'*18,end='')
                    return res_login
                else:
                    print('Не вірні данні')

        except KeyboardInterrupt:
            print(':`( Пакєда')
            exit()
        except ValueError:
            print('Користувач відсутній')
            continue

def menu():
    
    return str('\nВведіть дію:\n 1. Продивитись баланс\n 2. Поповнити баланс\n 3. Зняти з балансу \n 4. Історія\n 5. Вихід\n 0. Інкассація')

def menu_admin():
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
                        print(menu_admin())
                        return True
                    else:
                        print(menu())
                        return True
            except ValueError:
                print('Не вірна операція!')
                continue

def view_balance(user):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()
    with con:
        res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
        res_usr_id_fetch = res_usr_id.fetchone()[0]
        [res_balalance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))
        print(f'Баланс: {res_balalance}')
    return continue_or_exit(user)
        
def deposit(user):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()

    while True:
        try:
            with con:
                deposit = int(input('Введіть сумму депозиту --> '))

                if deposit < 0:
                    print('Депозит не може бути відємним =)')
                    continue
                else:
                    res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
                    res_usr_id_fetch = res_usr_id.fetchone()[0]
                    [old_balance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))

                    new_balance = old_balance + deposit

                    c.execute("""UPDATE balance SET balance=? WHERE login_id=?""",(new_balance,res_usr_id_fetch))
                    con.commit()
                    print(f'Баланс: {new_balance}')
                
                transactions(user)

            return continue_or_exit(user)
        except ValueError:
            print('Не допустимі символи')
            continue

def withdraw(user):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()
    
    while True:
        try:
            with con:
                withdraw = int(input('Введіть сумму Зняття --> '))
                if pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(withdraw, user):

                    if withdraw < 0:
                        withdraw *= -1
                        
                    res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
                    res_usr_id_fetch = res_usr_id.fetchone()[0]
                    [old_balance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))
                    
                    if old_balance < withdraw:
                        print("Не достатньо коштів на рахунку")
                        continue
                    else:
                        new_balance = old_balance - withdraw
                        c.execute("""UPDATE balance SET balance=? WHERE login_id=?""",(new_balance,res_usr_id_fetch))
                        con.commit()
                        print(f'Баланс: {new_balance}')
                    
                        transactions(user)

                        return continue_or_exit(user)
                else:
                    print("Помилка")
                    continue

        except ValueError:
            print('Не допустимі символи')
            continue

def transactions(user):

    pass
    '''try:
        with open(path + user + "_transactions.data", 'r' , encoding='utf-8') as user_transactions:
            print(f'Історія транзакцій {user} : \n{user_transactions.read()}')
    except FileNotFoundError:
        print('>>> Історія відсутня <<<')

    return continue_or_exit(user)'''

def view_collection(user):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()
    
    try:
        with con:
            c.execute("SELECT * FROM nominals")
            for row in c.fetchall():
                print(f'Номінал - {row[0]} = {row[1]} шт. ')

    except FileNotFoundError:
        print('>>> Історія відсутня <<<')

    return continue_or_exit(user)

def change_nominal(nominal):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()

    while True:
        operation = input('Введіть операцію (+xxx or -xxx) --> ')
        try:
            if operation[0] == '+':
                with con:            
                    [res_nom], = c.execute("""SELECT nominal FROM nominals WHERE id=?""",(nominal,))
                    new_nom = res_nom + int(operation)
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(new_nom,nominal))
                    con.commit()
                return True

            elif operation[0] == '-':
                with con:            
                    [res_nom], = c.execute("""SELECT nominal FROM nominals WHERE id=?""",(nominal,))
                    new_nom = res_nom + int(operation)
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(new_nom,nominal))
                    con.commit()
                return True   
            else:
                print('>>> Помилкова операція <<<')
                continue
        except ValueError:
            print('>>> Помилкова операція <<<')
            continue

def pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(amount, user):
    con = sqlite3.connect(db_path+db_file)
    c = con.cursor()
    summ_in_term = 0

    with con:
        con.row_factory = sqlite3.Row
        c.execute("""SELECT * FROM  nominals""")
        rows = c.fetchall()
        for row in rows:
            summ_in_term +=row[0]*row[1]
        print(amount)
        try:
            if amount % 10 > 0 :
                raise NoNominal 
            elif amount > summ_in_term:
                raise NoMoney
            else:
                dict_res = {}
                for row in rows:
                    dict_res.update({row[0]:row[1]})
                print(dict_res)

                summa = 0
                res = {}
                '''nom_10,nom_20,nom_50,nom_100,nom_200,nom_500,nom_1000 = 0,0,0,0,0,0,0
                while amount > 0:
                    while amount % 20 == 10:
                        nom_50 += 1
                        amount -= 50
                    while amount % 10 == 0:
                        nom_10 += 1
                        amount -= 10
                    while amount % 20 == 0:
                        nom_20 += 1
                        amount -= 20
                    while amount % 100 == 0:
                        nom_100 += 1
                        amount -= 100
                    while amount % 200 == 0:
                        nom_200 += 1
                        amount -= 200
                    while amount % 500 == 0:
                        nom_500 += 1
                        amount -= 500
                    while amount % 1000 == 0:
                        nom_1000 += 1
                        amount -= 1000
                    res = [nom_10,nom_20,nom_50,nom_100,nom_200,nom_500,nom_1000]
                    print("Видано: ")
                    for i in res:
                        if i > 0:
                            print(f"{i} ")'''
                    
                print(sorted(dict_res.items(), key=lambda x: -int(x[0])))
                for key, value in sorted(dict_res.items(), key=lambda x: -int(x[0])):
                    value = 0
                    
                    while summa + int(key) <= amount:
                        if dict_res[key] <= 0:
                            continue
                        else:    
                            summa += int(key)
                            dict_res[key] -= 1
                            value += 1
                            res.update({key:value})  
                print(res)
                print("Видано: ")
                for row in rows:
                    print(f"{row[0]} купюр по {row[1]}")
                return True

        except NoNominal:
            print('Сумма має бути кратна 10!')
            return False

        except NoMoney:
            print("Не достатньо коштів в терміналі")
            return False

        #except:
            #print('err')
        
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

        if user == 'admin':
            while True:
                print(menu_admin())
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
                except ValueError:
                    print('Не вірна операція!')
                    continue
                else:
                    print('Не вірна операція!')
                    continue

start()



