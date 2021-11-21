'''1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.'''

num = int(input('Enter number of strings -->' ))
str_list = list()
concat_string = ''

# add element to list
for i in range(num):
    string_ = input('Enter string ' + str(i+1) + ' -->')
    
    # if string is alpha
    if string_.isalpha():
        str_list.append(str(string_))
    
    # if string is digit
    elif string_.isdigit():
        str_list.append(int(string_))

    # else
    else:
        str_list.append(string_)

    # concat element from list
    print('List --> ', str_list)
    concat_string = concat_string + str(str_list[i])
    i += 1
    continue

# check for empty string
if not concat_string:
    print('Empty string')
else:
    print('Concat elements from list --> "'+concat_string+'"')