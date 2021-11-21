'''HARDCORE'''
def create_dict(_dict):  
        num_of_element = int(input('Enter number elements for DICT --> '))
        for i in range(num_of_element):
            element_dict = str(input("Enter 'key':'value' for " + str(i+1) + ' element on DICT --> '))
            key_value = list(element_dict.split(':'))
            _dict.update({key_value[0]:key_value[1]})
        return _dict

dict_1, dict_2, dict_3 = {}, {}, {}

dict_1 = create_dict(dict_1)
dict_2 = create_dict(dict_2)
dict_3 = create_dict(dict_3)

dict_1.update(dict_2)
dict_1.update(dict_3)

print(dict_1)
print(dict_2)
print(dict_3)