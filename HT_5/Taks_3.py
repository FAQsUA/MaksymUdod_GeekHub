''' 3. На основі попередньої функції створити наступний кусок кода:
        а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
        б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
        
        Name: vasya
        Password: wasd
        Status: password must have at least one digitas
        -----
        Name: vasya
        Password: vasyapupkin2000
        Status: OK
        P.S. Не забудьте використати блок try/except ;) '''
import re

class WRONG_Log(Exception):
    pass

def _check(login, password):

    digit = 0
    for element in str(password):
        if element.isdigit():
            digit += 1
    
    spec_symbol = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    flag_l = spec_symbol.search(login)
    flag_p = spec_symbol.search(password)

    status = {0:'OK',
              1:'Error in login / length min 3, max 50 symbols',
              2:'Error in login / characters are not supported',
              3:'Error in password / length min 8 symbols (there must be at least one digit)',
              4:'Error in password / characters are not supported',
              5:'Error in login and password /',
              6:'Error in login and password / characters are not supported'}

    if flag_l and flag_p:
        return status[6]
    elif flag_l:
        return status[2]
    elif flag_p:
        return status[4]
    else:

        if (len(login) < 3 or len(login) > 50) and (len(password) < 8 or digit == 0):
            try:
                raise WRONG_Log()
            except WRONG_Log:
                return status[5]

        elif len(login) < 3 or len(login) > 50:
            try:
                raise WRONG_Log()
            except WRONG_Log:
                return status[1]

        elif  len(password) < 8 or digit == 0:
            try:
                raise WRONG_Log()
            except WRONG_Log:
                return status[3]
                
        else:
            return status[0]
            
account_list = [{'name1':'passwd10'},{'name2': 'passwd2'},{'na': 'passwd30'}, {'1':'2'}, {'aaa#':'aaaaa1#'},{'aaadf':'aaaaa1#'}, {'aaa#':'aaaaa1sdfsd'}]

for element in account_list:
    for key, value in element.items():

        print(f'\nLogin: {key} \nPassword: {value} \nStatus: {_check(key, value)}\n')
