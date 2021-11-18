color_list1 = set(input('Enter the list_1 element through "," --> ').split(','))
color_list2 = set(input('Enter the list_2 element through "," --> ').split(','))

color_list = color_list1 - color_list2

print(color_list)