''' 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити! '''

def calc(num_1,num_2,operator_):

    if operator_ == '+':
        return print('Result =', num_1 + num_2)

    elif operator_ == '-':
        return print('Result = ', num_1 - num_2)

    elif operator_ =='*':
        return print('Result = ', num_1 * num_2)
    elif operator_ == '/':
        return print('Result = ', num_1 / num_2)

    else:
        print('WRONG >=( ')

number_1 = float(input('Enter number 1 --> '))
operator = str(input('Enter ( +, -, *, /) --> '))
number_2 = float(input('Enter number 2 --> '))
    
calc(number_1, number_2, operator)