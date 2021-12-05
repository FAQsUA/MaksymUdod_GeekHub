''' 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
        - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
        - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
        - щось своє :)
        Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом. '''
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
        raise WRONG_Log(status[6])
    elif flag_l:
        raise WRONG_Log(status[2])
    elif flag_p:
        raise WRONG_Log(status[4])
    else:

        if (len(login) < 3 or len(login) > 50) and (len(password) < 8 or digit == 0):
            raise WRONG_Log(status[5])

        elif len(login) < 3 or len(login) > 50:
            raise WRONG_Log(status[1])

        elif  len(password) < 8 or digit == 0:
            raise WRONG_Log(status[3])
                
        else:
            return print(f'Login: {login} \nPassword: {password}')

login_ = input('Enter login --> ')

password_ = input('Enter password --> ')

_check(login_, password_)


