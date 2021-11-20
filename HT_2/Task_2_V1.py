'''Standart'''

tuple_list = [(1,10),(2,2,20),(3,3,3,30)]
change_tuple_list = []
fake_tuple = []

print('List --> ', tuple_list)

change_element = input('Enter Number or String for change List of tuple --> ')

for i in range(0, len(tuple_list)):
    # take tuple from list
    fake_tuple = list(tuple_list[i])
    # change last element on tuple 
    fake_tuple[-1] = change_element
    # add new tuple to new list
    change_tuple_list.append(tuple(fake_tuple))

print('List --> ', change_tuple_list)
