# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fibonacci(num):
    fib1 = fib2 = 1
 
    print(fib1, fib2, end=' ')
 
    for i in iter(int,1):
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 <= num:
            print(fib2, end=' ')
        else:
            break

def easy_check():

    while True:
        value = input('Enter number --> ')
        
        if value.isdigit():
            if int(value) == 0 :
                print('\nWRONG / ',end=' ') 
                continue
            return int(value)
        
        elif value == 'exit':
            print('\n>>>>> EXIT <<<<<')
            return exit()
        
        else:
            print('\nWRONG / ',end=' ') 
            continue

number = easy_check()

if str(number).isdigit:
    fibonacci(number)