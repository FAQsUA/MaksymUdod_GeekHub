''' 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > 
    одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на 
    цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). 
    Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна 
    принтануть і вернуть суму, яка буде на рахунку. '''

def bank(money, years, percent=0.1):

    for i in range(int(years)):
        money += money*percent
    
    return print(f"Your money aster {years} years : {money:.3f}")

def easy_check():

    while True:
        value = input()
        
        if str(value).replace('.','').isdigit():
            return float(value)
        
        elif value == 'exit':
            print('\n>>>>> EXIT <<<<<')
            return exit()
        
        else:
            print('\nWRONG / ',end=' ') 
            continue

print('Enter money --> ', end='')
m = easy_check()

print('Enter years --> ',end='')
y = int(easy_check())

print('Enter percent --> ',end='')
p = easy_check()

if p >= 1:
    p = p/100

bank(m, y, p)