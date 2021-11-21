'''Use Func _ HARDCORE'''
#=======================================FUNCTION==========================================================

main_list = []

# видалення пустих елементів
def func_is_empty(elements):
    element_0 = [element for element in elements if element]
    return element_0

# елемент списку строка
def func_is_string():
    main_list.append(input('Enter String --> '))

# елемент списку список
def func_is_list():
    num_list_elements = int(input('Enter num of elements in List (enter 0 to create empty list) --> '))
    list_in_list = []
    
    if num_list_elements == 0:
        main_list.append(list_in_list)
    else:

        for i in range(num_list_elements):
            element = input('Enter element ' + str(i+1) + ' on LIST (enter "empty" to create empty element on list)--> ')
            # якщо користувач введе empty то елемент пропуститься тобто буде пустим
            if element == 'empty':
                continue
            else:
                # якщо ні елемент буде дрдано в список
                list_in_list.append(element)
        # додання елемента список в головний список
        main_list.append(list_in_list)

# елемент списку кортеж
def func_is_tuple():
    num_tuple_elements = int(input('Enter num of elements in Tuple (enter 0 to create empty tuple) --> '))
    fake_tuple = []
    
    if num_tuple_elements == 0:
        main_list.append(tuple(fake_tuple))
    else:
        for i in range(num_tuple_elements):
        # аналогічно як зі списком
            element = input('Enter element ' + str(i+1) + ' on TUPLE (enter "empty" to create empty element on tuple) --> ')
            if element == 'empty':
                continue
            else:
                fake_tuple.append(element)
        main_list.append(tuple(fake_tuple))

# елемент списку словник
def func_is_dict():
    num_dict_elements = int(input('Enter num of elements in Dict (enter 0 to create empty dict) --> '))
    fake_dict = {}
    
    if num_dict_elements == 0:
        main_list.append(fake_dict)
    else:
        for i in range(num_dict_elements):
            # аналогічно як зі списком
            element = str(input("Enter 'key':'value' for " + str(i+1) + ' element on DICT (enter "empty" to create empty element on dict) --> '))
            key_value = []

            if element == 'empty':
                continue
            else:
                key_value = list(element.split(':'))
                fake_dict.update({key_value[0]:key_value[1]})
                key_value.clear()

            i += 1
        main_list.append(fake_dict)

#=======================================BODY_CODE==========================================================       

num_of_elements = int(input('\nEnter number of elements in list --> '))

for i in range(num_of_elements):
    type_element = str(input('Enter TYPE of '+ str(i+1) + ' element in list (String, List, Tuple, Dict ?) --> '))
    # перевіряєм який тип елемента обрав користувач
    while True:
        if type_element == 'String':
            func_is_string()
        elif type_element == 'List':
            func_is_list()
        elif type_element == 'Tuple':
            func_is_tuple()
        elif type_element == 'Dict':
            func_is_dict()
        else:
            ''' 
            Якщо значення не вірне зипатає повторного введення. 
            Після успішного введення вийде з циклу та перейде 
            до перевірки іншого елементу
            '''
            print('Wrong!')
            type_element = str(input('Enter TYPE of '+ str(i+1) + ' element in list (String, List, Tuple, Dict ?) --> '))
            continue

        break
    
print('\nTest list -->', main_list)
print('\nDel empty element -->', func_is_empty(main_list))