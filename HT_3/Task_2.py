''' 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який 
виведе всі високосні роки в цьому проміжку (границі включно). '''

start_year = int(input('Enter start year --> '))
end_year = int(input('Enter end year --> '))

for year in range(start_year, end_year+1):
    if (year % 400 == 0) or (year % 4  == 0) and (year % 100 != 0):
        print(year)
