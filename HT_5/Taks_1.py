''' 1.  Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
        Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - 
        необов'язковий параметр <silent> (значення за замовчуванням - <False>).
        Логіка наступна:
            якщо введено коректну пару ім'я/пароль - вертається <True>;
            якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, 
            інакше (<silent> == <False>) - породжується виключення LoginException '''

class LoginException(Exception):
    pass

def logpass(name, password, silent=False):
    account_list = [{'name_1':'paswd_1'},{'name_2': 'paswd_2'},{'name_3': 'paswd_3'},{'name_4': 'paswd_4'},{'admin': 1}]

    for element in account_list:
        for key in element:

            if key == name and element[key] == password:
                return True
            else:
                if silent == True:
                    return False
                else:
                    raise LoginException('ALERT !!!')

def easy_check():

    while True:
        value = str(input())
        
        try:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            elif value == '':
                return None
            else:
                print('WRONG !!! Enter True or False -->', end=' ')
                continue
        except KeyboardInterrupt:
            print('>>>>> EXIT <<<<<')
            exit()

login = input('Enter Login --> ')
passwd = input('Enter Password --> ')

print('Checkbox True or False ? --> ', end=' ')
silent_ = easy_check()

print(logpass(login, passwd, silent_))