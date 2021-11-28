# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.
from math import sqrt

def is_prime(number):
    Tru_Fal = True

    if(number > 1):
        for i in range(2, int(sqrt(number)) + 1):
            if (number % i == 0):
                Tru_Fal = False
                break
        if Tru_Fal:
            return True
        else:
            return False
    else:
        return False


while True:
    number = input('Enter number from 0 to 1000 inclusive --> ')
    try:
        if number.isdigit() and (0 <= int(number) <= 1000):
            print('\n'+ str(is_prime(int(number))) + '\n')
            continue

        elif number == 'exit':
            print('\n>>>>> EXIT <<<<<')

        else:
            print('\nWRONG / ',end=' ') 
            continue 

    except:
        print('\nWRONG / ',end=' ') 
        continue