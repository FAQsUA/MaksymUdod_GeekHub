num_of_element = int(input('Enter number of elements in DICT --> '))
dict_dupl = {}
dict_final = {}
# create new dict with number "num_of_element"
for i in range(num_of_element):
    element_dict = str(input("Enter 'key':'value' for " + str(i+1) + ' element on DICT  --> '))
    key_value = list(element_dict.split(':'))
    # add elements to new dict
    dict_dupl.update({key_value[0]:key_value[1]})

print('Dict --> ', dict_dupl)
# create new dict without duplicates
for key, value in dict_dupl.items():
    if value not in dict_final.values(): 
        dict_final[key] = value # write item from dict_dupl to dict_final, use key from dict_dupl

print('Final dict --> ', dict_final)
