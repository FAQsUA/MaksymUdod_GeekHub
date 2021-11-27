# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calc(number_one,number_two,operand):

    if operand == '+':
        return print('Result =', number_one + number_two)

    elif operand == '-':
        return print('Result = ', number_one - number_two)

    elif operand =='*':
        return print('Result = ', number_one * number_two)

    elif operand == '/':

        if number_two == 0:
            print('WRONG!!! division by zero')
        else:
            return print('Result = ', number_one / number_two)


num_1 = 0
num_2 = 0
operator_2 = ''

while True:
    number_1 = str(input('Enter number 1 --> '))
    
    if number_1.replace('.','').isdigit():
    
        num_1 = float(number_1)
        
        while True:
            operator_1 = str(input('Enter ( +, -, *, /) --> '))

            if operator_1 in ('+', '-', '*', '/'):
                operator_2 = str(operator_1)

                while True:
                    number_2 = str(input('Enter number 2 --> '))

                    if number_2.replace('.','').isdigit():
                        num_2 = float(number_2)

                        calc(num_1, num_2, operator_2)

                        break
                    elif number_2 == 'exit':
                        print('>>>>>EXIT<<<<<')
                        break
                    elif not number_2.isdigit():
                        print('WRONG is not digit >=( ')
                        continue
                break

            elif operator_1 == 'exit':
                print('>>>>>EXIT<<<<<')
                break
            else:
                print('WRONG is not operand >=( ')
                continue

        break

    elif number_1 == 'exit':
        print('>>>>>EXIT<<<<<')
        break
    elif not number_1.isdigit():
        print('WRONG is not digit >=( ')
        continue
    break