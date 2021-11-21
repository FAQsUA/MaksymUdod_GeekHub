'''HARDCORE lol'''

num_of_element = int(input('Enter positive integer --> '))

dict_ = {}
for i in range(num_of_element+1):
    dict_.update({i:i*i})

print(dict_)