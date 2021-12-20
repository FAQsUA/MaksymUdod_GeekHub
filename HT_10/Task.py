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
import request_module


db_path = os.path.dirname(os.path.realpath(__file__)) + '/'
db_file = 'atm.db'
db = db_path+db_file


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


def ins_in_tab_transactions(con, sql_trs):
    try:
        sql = '''INSERT or IGNORE INTO transactions (login, operation, amount) 
                        VALUES(?,?,?)'''
        c = con.cursor()
        c.execute(sql, sql_trs)
        con.commit()
    except Error as err:
        print(err)


def create_db():
    con = connection(db)
    
    if os.path.exists(db):
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
                                id text PRIMARY KEY,
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
                balance = (i,login_id,str(i*1000))
                ins_in_tab_balance(con,balance)

            nominals = ["10","20","50","100","200","500","1000"]
            for item in nominals:
                nominal = (item,5)
                ins_in_tab_nominals(con,nominal)
        
    else:
        pass
        

create_db()
#########>>>DATABASE CONFIGURATION END<<<#########################################################################


class NoMoney(Exception):
    pass


class NoNominal(Exception):
    pass


def validation():
    con = sqlite3.connect(db)
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
    
    return str('\nВведіть дію:\n 1. Продивитись баланс\n 2. Поповнити баланс\n 3. Зняти з балансу \n 4. Історія\n 5. Курс валют\n 6. Вихід\n 0. Інкассація')


def menu_admin():
    return str('\nВведіть дію:\n 1. Переглянути наявні купюри\n 2. Змінити кількість купюр\n 3. Змінити користувача\n 4. Вихід')


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
    con = sqlite3.connect(db)
    c = con.cursor()
    with con:
        res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
        res_usr_id_fetch = res_usr_id.fetchone()[0]
        [res_balalance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))
        print(f'Баланс: {res_balalance}')
    return continue_or_exit(user)


def deposit(user):
    con = sqlite3.connect(db)
    c = con.cursor()

    while True:
        try:
            deposit = int(input('Введіть сумму депозиту --> '))

            if deposit < 0:
                print('Депозит не може бути відємним =)')
                continue
            else:
                break
        except ValueError:
            print('Не допустимі символи')
            continue
    with con:
        res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
        res_usr_id_fetch = res_usr_id.fetchone()[0]
        [old_balance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))

        new_balance = old_balance + deposit

        c.execute("""UPDATE balance SET balance=? WHERE login_id=?""",(new_balance,res_usr_id_fetch))
        con.commit()
        print(f'Баланс: {new_balance}')
    
    transactions(user, 'Пополнение', deposit)

    return continue_or_exit(user)


def withdraw(user):
    con = sqlite3.connect(db)
    c = con.cursor()
    
    while True:
        try:
            withdraw = int(input('Введіть сумму Зняття --> '))

            if withdraw < 0:
                withdraw *= -1

            with con:   
                res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
                res_usr_id_fetch = res_usr_id.fetchone()[0]
                [old_balance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))                    
                if old_balance < withdraw:
                    print("Не достатньо коштів на рахунку")
                    continue
                else:
                    if pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(user, withdraw):
                        transactions(user,'Снятие', withdraw)

            return continue_or_exit(user)   
        except ValueError:
            print('Не допустимі символи')
            continue


def transactions(user, operator, amount):
    con = sqlite3.connect(db)
    c = con.cursor()
    sql_c_tab_trs = """CREATE TABLE IF NOT EXISTS transactions (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        login text NOT NULL,
                        operation text NOT NULL,
                        amount integer NOT NULL);"""  
    if con:
        create_table(con, sql_c_tab_trs)
        
    sql_trs = (user,operator, amount)
    with con:
        ins_in_tab_transactions(con,sql_trs)


def view_transactions(user):
    con = sqlite3.connect(db)
    c = con.cursor()
    with con:
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='transactions' ''')
        if c.fetchone()[0] == 1:
            text = c.execute(''' SELECT login, operation, amount FROM transactions WHERE login=? ''',(user,))
            for tr_text in text.fetchall():
                print(f"{tr_text[1]} на сумму {tr_text[2]}")
           
        else:
            print(">>> Історія відсутня")
    return True


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
                    if (int(operation) + res_nom) < 0:
                        print('>>> Помилкова операція / Вкажіть меншу кількість <<<')
                        continue 
                    else:
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


def pisets_zadolbalo_rabotai_lol_kak_ya_golovu_lomal(user, amount):
    con = sqlite3.connect(db)
    c = con.cursor()

    con.row_factory = sqlite3.Row
    c.execute("""SELECT * FROM  nominals""")
    rows = c.fetchall()
    dict_nominals = dict({item for item in rows})

    money = amount

    nominals = [int(element) for element in dict_nominals.keys() if dict_nominals[element] != 0]
    sum_in_atm = sum([int(key) * vvalue for key, vvalue in dict_nominals.items()])

    try:
        if amount % 10 > 0 :
            raise NoNominal 
        elif amount > sum_in_atm:
            raise NoMoney
        else:
                
            give_nominal = {'1000': 0, '500': 0, '200': 0, '100': 0, '50': 0, '20': 0, '10': 0}
            flag = True
        with con:
            while flag:
                flag = False
                if money // 1000 > 0 and dict_nominals['1000'] != 0 and \
                        ((money - 1000) == 0 or [item for item in nominals if ((money - 1000) // item) > 0]):
                    dict_nominals['1000'] -= 1
                    give_nominal['1000'] += 1
                    money -= 1000
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['1000'],'1000'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 500 > 0 and dict_nominals['500'] != 0 and \
                        ((money - 500) == 0 or [item for item in nominals if ((money - 500) // item) > 0]):
                    dict_nominals['500'] -= 1
                    give_nominal['500'] += 1
                    money -= 500
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['500'],'500'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 200 > 0 and dict_nominals['200'] != 0 and \
                        ((money - 200) == 0 or [item for item in nominals if ((money - 200) // item) > 0]):
                    dict_nominals['200'] -= 1
                    give_nominal['200'] += 1
                    money -= 200
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['200'],'200'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 100 > 0 and dict_nominals['100'] != 0 and \
                        ((money - 100) == 0 or [item for item in nominals if ((money - 100) // item) > 0]):
                    dict_nominals['100'] -= 1
                    give_nominal['100'] += 1
                    money -= 100
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['100'],'100'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 50 > 0 and dict_nominals['50'] != 0 and \
                        ((money - 50) == 0 or [item for item in nominals if ((money - 50) // item) > 0]):
                    dict_nominals['50'] -= 1
                    give_nominal['50'] += 1
                    money -= 50
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['50'],'50'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 20 > 0 and dict_nominals['20'] != 0 and \
                        ((money - 20) == 0 or [item for item in nominals if ((money - 20) // item) > 0]):
                    dict_nominals['20'] -= 1
                    give_nominal['20'] += 1
                    money -= 20
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['20'],'20'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
                elif money // 10 > 0 and dict_nominals['10'] != 0 and \
                        ((money - 10) == 0 or [item for item in nominals if ((money - 10) // item) > 0]):
                    dict_nominals['10'] -= 1
                    give_nominal['10'] += 1
                    money -= 10
                    c.execute("""UPDATE nominals SET nominal=? WHERE id=?""",(dict_nominals['10'],'10'))
                    con.commit()
                    if money == 0:
                        break
                    else:
                        flag = True
            result = [int(key) * value for key, value in give_nominal.items()]
            if not sum(result):
                raise NoMoney
            if sum(result) == amount:
                res = {}
                for key, value in give_nominal.items():
                    if value == 0:
                        continue
                    res[key] = value
                
            print(f'Видано {sum(result)}')
            print('Номіналами: ', end="")

            for key, value in res.items():
                print(f'{key} - {value}', end=' ')

               
            res_usr_id = c.execute("""SELECT id FROM users WHERE login=?""",(user,))
            res_usr_id_fetch = res_usr_id.fetchone()[0]
            [old_balance], = c.execute("""SELECT balance FROM balance WHERE login_id=?""",(res_usr_id_fetch,))                    
            new_balance = old_balance - amount

            c.execute("""UPDATE balance SET balance=? WHERE login_id=?""",(new_balance,res_usr_id_fetch))
            con.commit()

            print(f'\nБаланс: {new_balance}')

        return True
            
    except NoNominal:
        print('Введіть сумму кратну 10 !!!')
    except NoMoney:
        print('Не достатньо коштів в банкоматі !!!')


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
    flag = True
    print('\nВас вітає Фуфло Банк\n')
    while True:
        user = validation()

        if user == 'admin':
            while flag:
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
                            flag = False
                            break

                        elif int(operation) == 4:
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
                        if view_transactions(user):
                            continue

                    elif int(operation) == 5:
                        if request_module.start():
                            continue

                    elif int(operation) == 6:
                        print(':`( Пакєда')
                        exit()
                    elif int(operation) == 0:
                        flag = True
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



