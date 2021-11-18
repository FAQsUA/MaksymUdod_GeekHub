new_list = list(input('Enter List element through "," --> ').split(','))
new_tuple = tuple(input('Enter Tuple element through "," --> ').split(','))
number = input('Enter Number for search -->')
print(new_list)
print(new_tuple)

if number in new_list:
    print(True)
else:
    print(False)
if number in new_tuple:
    print(True)
else:
    print(False)