'''Hardcore'''

print("\nСhange the last element of the tuple that is in the list")
print('____________________________________________________\n\n')

num_elements_on_list = int(input('Enter number of Tuples in list -->'))

tuple_list = []
change_tuple_list = []
fake_tuple = []

for i in range(num_elements_on_list):
    num_elements_on_tuple = int(input('Enter number of elements on ' + str(i+1) +  ' - TUPLE --> '))
    
    for num in range(num_elements_on_tuple):
        fake_tuple.append(input('Enter digit, leter, or symbols for ' + str(num+1) + ' element in Tuple ' + str(i+1) + '--> '))

    tuple_list.append(tuple(fake_tuple))
    fake_tuple.clear()

print('\nList --> ', tuple_list)

change_element = input('\nEnter Number or String for change last element for all Tuples in List --> ')

for num in range(len(tuple_list)):
    # take tuple from list
    fake_tuple = list(tuple_list[num])
    # change last element on tuple
    fake_tuple[-1] = change_element
    # add new tuple to new list
    change_tuple_list.append(tuple(fake_tuple))

print('\nChange list --> \n', change_tuple_list)