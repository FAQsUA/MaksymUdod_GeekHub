''' 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
        - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
        - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
        - щось своє :)
        Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом. '''

class WRONG_Log_Pass(Exception):
    pass

def login_check():
    value = input('Enter Login --> ')

    if len(value) < 3 or len(value) > 50:
        raise WRONG_Log_Pass('WRONG !!! login length min 3, max 50 symbols')
    else:
        return value

def password_check():
    value = input('Enter Password --> ')

    digit = 0

    for element in value:
        if element.isdigit():
            digit += 1

    if len(value) < 8 or digit == 0:
        raise WRONG_Log_Pass('WRONG !!! password length min 8 symbols (there must be at least one digit)')
    else:
        return value


login_ = login_check()
password_ = password_check()

print(f'Login: {login_} \nPassword: {password_}')