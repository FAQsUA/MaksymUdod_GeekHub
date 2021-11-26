# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь) 

def season(mon):
    
    if mon in (12,1,2):
        print("Зима")
    elif mon in (3,4,5):
        print("Весна")
    elif mon in (6,7,8):
        print("Літо")
    elif mon in (9,10, 11):
        print("Осінь")
while True:
    mon = input("Enter mon --> ")
    if mon.isdigit():
        season(int(mon))
    elif mon =='exit':
        break
    else:
        print('is not digit')
        continue

