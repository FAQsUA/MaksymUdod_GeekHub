'''Standart'''

test_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
test_list_2 = []

for element in test_list:
    if element:
        test_list_2.append(element)
print('Test list -->', test_list)
print('Del empty element -->', test_list_2)      