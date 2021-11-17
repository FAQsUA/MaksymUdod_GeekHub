# WITHOUT LISTs

# проверка натуральности числа
def isInt(n):
    return int(n) == float(n)

num = float(input('Enter number --> '))
sum_num = 0

while True:
    # проверка + или - числа
    if float(num) < 0: 
        print('Enter natural number')
        num = float(input('Enter number --> '))
        continue
    # проверка числа на int/float
    elif isInt(num) == False:
        print('Enter natural number')
        num = float(input('Enter number --> '))
        continue
    # сумма всех натуральных чисел заданого пользователем
    else:
        while int(num) > 0:
            sum_num += num
            num -= 1
    break # выход из цикла
print('Summ: ',int(sum_num))
