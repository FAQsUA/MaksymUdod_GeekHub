# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

while True:
    number = input('Enter number --> ')
    try:
        if int(number) > 0:
            print(number + ' > 0 =', int(number)**2, '(**2)')
            
        elif int(number) < 0:
            print(number + ' < 0 =', int(number)+100, '(+100')
        elif int(number) == 0:
            print(number + ' = 0 =', int(number), '()')
        
    except:
        if number == 'exit':
            break
        else:
            print('\nWRONG / ',end=' ') 
            continue

