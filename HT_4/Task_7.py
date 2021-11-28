# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
from collections import Counter

def easy_check():

    while True:
        value = input('Enter number elements in list --> ')
        
        if str(value).isdigit():
            return int(value)
        
        elif value == 'exit':
            print('\n>>>>> EXIT <<<<<')
            return exit()
        
        else:
            print('\nWRONG / ',end=' ') 
            continue

def list_chek(list_):
    count = 0
    dict_list = Counter(list_)
    for key, value in dict_list.items():
        if value > 1:
            print (str(key) + ' - ' + str(value) + ' повторення ')
            count = 1
        
    if count == 0:
        print('Немає повтореннь')
    

simple_list = []
element = easy_check()

for i in range(0, int(element)):
        simple_list.append(input('Enter list element ' + str(i+1)+ ' --> '))

list_chek(simple_list)