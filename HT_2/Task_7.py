'''
7. Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
                Вихідний результат:
                MIN: 10
                MAX: 60'''

# Standart

num_of_element = int(input('Enter number of elements in DICT --> '))

dict_ = {}
# create new dict with number "num_of_element"
for i in range(num_of_element):
    element_dict = str(input("Enter 'key':'value' for " + str(i+1) + ' element on DICT  --> '))
    key_value = list(element_dict.split(':'))
    # add elements to dict
    dict_.update({key_value[0]:key_value[1]})

print('Dict --> ', dict_)
print('min = ', min(dict_.values())) # min values in dict
print('max = ', max(dict_.values())) # max values in dict

