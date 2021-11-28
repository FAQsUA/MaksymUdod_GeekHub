# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

def list_prime(number_one, number_two):
    list_p = []
    for number in range(number_one,number_two + 1):
        if number > 1:
            if all(number % i !=0 for i in range(2,number)):
                list_p.append(number)
    return list_p

while True:
    number_1 = input('Enter number one --> ')

    if number_1.isdigit():

        try:
            while True:
                number_2 = input('Enter number two --> ')

                if number_2.isdigit():

                    try:
                        print('\n', list_prime(int(number_1), int(number_2)), '\n')
                        break
                    except:
                        print('\nWRONG / ',end=' ') 
                        continue

                elif number_2 == 'exit':
                    print('\n>>>>> EXIT <<<<<')
                    break

                else:
                    print('\nWRONG / ',end=' ') 
                    continue
        except:
            print('\nWRONG / ',end=' ') 
            continue

    elif number_1 == 'exit':
            print('\n>>>>> EXIT <<<<<')
            break

    else:
        print('\nWRONG / ',end=' ') 
        continue 
    break