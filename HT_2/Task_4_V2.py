'''HARDCORE'''

num_of_dict = int(input('Enter number of DICT --> '))
dict_final = {}

for i in range(num_of_dict):
    dict_in = {}
    element = int(input("Enter number elements for " + str(i+1) + ' DICT --> '))

    for n in range(element):
        element_dict = str(input("Enter 'key':'value' for " + str(n+1) + ' element on DICT ' + str(i+1) + ' --> '))
        key_value = list(element_dict.split(':'))
        dict_in.update({key_value[0]:key_value[1]})

    dict_final.update(dict_in)

print(dict_final)
