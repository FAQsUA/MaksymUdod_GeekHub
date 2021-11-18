# create list from enter dec numbers
dec_nums = input('Enter Dec numbers through "," --> ').split(',')
# create list hex numner, using hex() and del 0x
hex_nums = [hex(int(i))[2:] for i in dec_nums]

print('Out Hex Numbers --> {0}'.format(','.join(hex_nums)))
