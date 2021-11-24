''' 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову,
 яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0. '''

while True:
    num_for_for = input('Enter number --> ')

    if num_for_for == 'exit':
        break
    elif num_for_for.isdigit():
        for number in range(0,int(num_for_for)+1):
            if number % 17 == 0 and number != 0:
                print(number)  
    else:
        print('is not digit')
        continue


