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
class WRONG_Log_Pass(Exception):
    pass

def _check(login, password):

    digit = 0
    status = ''

    if len(login) < 3 or len(login) > 50:
        status = 'WRONG !!! login length min 3, max 50 symbols'
    else:
        status = 'OK'
    
    for element in str(password):
        if element.isdigit():
            digit += 1

    if len(password) < 8 or digit == 0:
        if status == 'OK':
            status = 'WRONG !!! password length min 8 symbols (there must be at least one digit)'
        else:
            status = status + ' and password length min 8 symbols (there must be at least one digit)'
    
    return status


account_list = [{'name_1':'paswd_10'},{'name_2': 'paswd_2'},{'na': 'paswd_30'}, {'1':'2'}]

for element in account_list:
    for key, value in element.items():
        print(f'Login: {key} \nPassword: {value} \nStatus: {_check(key, value)}\n')
