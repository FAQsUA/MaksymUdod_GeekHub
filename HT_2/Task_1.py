num = int(input('Enter number of strings -->' ))
str_list = []
concat_string = ''
i = 0
# add element to list
for i in range(num):
    str_list.append(input('Enter string ' + str(i+1) + ' -->'))
# concat strings from list
    concat_string = concat_string + str_list[i] 
    i += 1
    continue
# check for empty string
if not concat_string:
    print('Empty string')
else:
    print('"'+concat_string+'"')