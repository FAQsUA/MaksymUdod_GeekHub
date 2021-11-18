dec_nums = input('Enter Dec numbers through "," --> ')
# create tuple from enter dec numbers
dec_list = tuple(dec_nums.split(','))
hex_list = ()

for i in dec_list:
    # Add new number to tuple hex_list and convert dec to hex
    hex_list += (hex(int(i)),)
    continue

print('Out Hex Numbers --> {0}'.format(','.join(hex_list)))
