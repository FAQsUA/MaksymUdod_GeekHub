# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.

# P.S. При виконанні завдання помітив що використовую повторно схожий код. Вирішив зробити функцію окремо для перевірки данних. Так ніби краще, ніж безкінечні
# цикли в безкінечних циклах. XD

def list_prime(number_one, number_two):
    list_p = []
    for number in range(number_one,number_two + 1):
        if number > 1:
            if all(number % i !=0 for i in range(2,number)):
                list_p.append(number)
    return list_p

def easy_check():

    while True:
        num = input('--> ')
        
        if num.isdigit():
            return int(num)
        elif num == 'exit':
            print('\n>>>>> EXIT <<<<<')
            return exit()
        else:
            print('\nWRONG / Enter number',end=' ') 
            continue
        

print('Enter number one ', end='')
number_1 = easy_check()
print('Enter number two ', end='')
number_2 = easy_check()

if str(number_1).isdigit and str(number_2).isdigit:
    print(list_prime(number_1,number_2))
