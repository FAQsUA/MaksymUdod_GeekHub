''' 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
        - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
        - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
        - щось своє :)
        Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом. '''

class WRONG_Log_Pass(Exception):
    pass

def _check(login, password):

    digit = 0

    if len(login) < 3 or len(login) > 50:
        raise WRONG_Log_Pass('WRONG !!! login length min 3, max 50 symbols')
    else:

        for element in str(password):
            if element.isdigit():
                digit += 1

        if len(password) < 8 or digit == 0:
            raise WRONG_Log_Pass('WRONG !!! password length min 8 symbols (there must be at least one digit)')
        else:
            return print(f'Login: {login} \nPassword: {password}')


login_ = input('Enter Login --> ')
password_ = input('Enter Password --> ')

_check(login_, password_)

