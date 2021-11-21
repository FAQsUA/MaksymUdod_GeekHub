'''4. Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

# Hardcore

num_of_dict = int(input('Enter number of DICT --> '))
dict_final = {}
# generete number of dict
for i in range(num_of_dict):
    dict_in = {}
    num_of_element = int(input("Enter number elements for " + str(i+1) + ' DICT --> '))
    # create new dict with number "element"
    for n in range(num_of_element):
        element_dict = str(input("Enter 'key':'value' for " + str(n+1) + ' element on DICT ' + str(i+1) + ' --> '))
        key_value = list(element_dict.split(':'))
        # add elements to new dict
        dict_in.update({key_value[0]:key_value[1]})
        
    # add new dict to main dict
    print('Dict ' + str(n+1) + ' --> ', dict_in)
    dict_final.update(dict_in)

print(dict_final)
