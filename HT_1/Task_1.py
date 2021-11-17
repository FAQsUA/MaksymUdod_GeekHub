# Version 1

nums = input('Enter numbers --> ') # enter numners

list_nums = nums.split(',') #create list without symbol ','
tuple_nums = tuple(list_nums) # create tuple

print('list:', list_nums)
print('Tuple:', tuple_nums)

# Version what i think be better
'''
import re

nums = input('Enter numbers --> ') # enter numners

list_nums = re.split(r';|,| +|\.', nums) # create list without symbols ; , . and " "
tuple_nums = tuple(list_nums) # create tuple

print('list:', list_nums)
print('Tuple:', tuple_nums)
'''