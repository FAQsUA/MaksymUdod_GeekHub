# WITH LISTs

# проверка натуральности числа
def isInt(n):
    return int(n) == float(n)

num = int(input('Enter list size --> '))
sum_num = 0
num_list = []
i = 0

for i in range(0,num):
    num_list.append(input('Enter number --> '))
    i += i
    continue

print(num_list)
    
for i in range(0,len(num_list)): 
    if isInt(float(num_list[i])) == False:
            i += i
            continue
    # проверка + или - числа
    elif int(num_list[i]) < 0:
        i = i+1
        continue
    else:
            sum_num += int(num_list[i])
 
print('Summ: ',int(sum_num))
