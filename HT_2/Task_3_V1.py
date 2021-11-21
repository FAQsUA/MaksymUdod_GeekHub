'''3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''

# Standart

test_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
test_list_2 = []

for element in test_list:
    if element:
        test_list_2.append(element)
print('Test list -->', test_list)
print('Del empty element -->', test_list_2)      