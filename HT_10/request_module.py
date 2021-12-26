from datetime import datetime, timedelta
import datetime
import requests

take_date_and_time = datetime.datetime.now()
str_today = take_date_and_time.strftime('%d.%m.%Y')
today_date = take_date_and_time.strptime(str_today, '%d.%m.%Y')
year = int(take_date_and_time.year)


def valute_des():
    print('Виберіть валюту: \n1. USD \n2. EUR')
    while True:
        try:
            des = input('--> ')
            if des.isdigit():
                return int(des)
            else:
                print('Error !!!')
                continue
        except ValueError:
            print('ValueError')


def do_cur_request(*args):
    r_to_cur_date = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    list_ex_rate = r_to_cur_date.json()
    if args:
        return list_ex_rate
    else:
        print(f"Дата: {today_date.strftime('%d.%m.%Y')}\nКурс відносно гривні: ")
        for item in range(len(list_ex_rate)):
            if 'ccy' in list_ex_rate[item]:
                print(f"{list_ex_rate[item]['ccy']} = {list_ex_rate[item]['sale']}")
            else:
                continue


def print_history(valuta, date):
    back_rate = 0
    count = 0
    delta_date = today_date - date
    for i in range(delta_date.days):
        back_day = date + timedelta(days=i - 1)
        day = date + timedelta(days=i)
        if count >= 1:
            r_to_back_date = requests.get(
                "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + back_day.strftime('%d.%m.%Y'))
            json_back_ex_rate = r_to_back_date.json()
            list_back_ex_rate = json_back_ex_rate['exchangeRate']
            for item in range(len(list_back_ex_rate)):
                for key, value in list_back_ex_rate[item].items():
                    if value == valuta:
                        back_rate = list_back_ex_rate[item]["saleRateNB"]
                        break
        r_to_date = requests.get(
            "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + day.strftime('%d.%m.%Y'))
        json_ex_rate = r_to_date.json()
        list_ex_rate = json_ex_rate['exchangeRate']

        for item in range(len(list_ex_rate)):
            for key, value in list_ex_rate[item].items():
                if value == valuta:
                    cur_rate = list_ex_rate[item]["saleRateNB"] - back_rate
                    if back_rate != 0:
                        print(
                            f' Date: {day.strftime("%d.%m.%Y")}  Curs: {list_ex_rate[item]["saleRateNB"]}    '
                            f'{"{0:.4f}".format(cur_rate)}')
                    else:
                        print(
                            f' Date: {day.strftime("%d.%m.%Y")}  Curs: {list_ex_rate[item]["saleRateNB"]}')
        count += 1


def do_request(date):
    r_to_date = requests.get("https://api.privatbank.ua/p24api/exchange_rates?json&date=" + date.strftime('%d.%m.%Y'))
    json_ex_rate = r_to_date.json()
    list_old_rate = json_ex_rate['exchangeRate']
    for item in range(len(list_old_rate)):
        if 'currency' in list_old_rate[item]:
            print(f"- {list_old_rate[item]['currency']} ")
        else:
            continue
    valuta = input('Введіть валюту --> ')
    print_history(valuta.upper(), date)
    return True


def rate_start():
    while True:
        try:
            date_input = input('Введіть дату (дд.мм.рррр) --> ')
            date_in = datetime.datetime.strptime(date_input, '%d.%m.%Y')
            if date_in > today_date:
                print('Error, input correct date')
                continue
            elif date_in == today_date:
                do_cur_request()
                break
            elif date_in < today_date:
                do_request(date_in)
                break
            else:
                print('err')
                continue
        except ValueError:
            print('Error, input correct date')
            continue
        except KeyboardInterrupt:
            print('goodbye')
            exit()
    return True


def convert(valuta, date):
    flag = True
    des_first = ''
    des_second = ''
    des_value = 0

    while flag:
        try:
            des_first = input('Виберіть першу валюту ( --> ')
            if des_first.upper() in valuta:
                while True:
                    try:
                        des_value = float(input(f'Введіть сумму для {des_first}--> '))
                    except ValueError:
                        print('Err !!!')
                        continue
                    if isinstance(des_value, float):
                        break
                    else:
                        print('Err !!!')
                        continue
                while True:
                    des_second = input('Виберіть другу валюту --> ')
                    if des_second.upper() in valuta:
                        if des_first == des_second:
                            print('Error !!!')
                            continue
                        else:
                            break
                    else:
                        print('Err !!!')
                        continue
                flag = False
            else:
                print('Err !!!')
                continue
        except ValueError:
            print('Error/ enter data correct !!!')
            continue
        except KeyboardInterrupt:
            print('goodbye')
            exit()

    r_to_date = requests.get(
        "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + date.strftime('%d.%m.%Y'))
    json_ex_rate = r_to_date.json()
    list_old_rate = json_ex_rate['exchangeRate']
    del list_old_rate[0]
    convert_ = 0
    for item in list_old_rate:

        if item['currency'] == des_first.upper():
            first_value = item['saleRateNB']
            for item_ in list_old_rate:
                if item_['currency'] == des_second.upper():
                    second_value = item_['saleRateNB']
                    convert_ = (float(first_value) * des_value) / float(second_value)
                    break
                else:
                    continue
            break
        else:
            continue
    print(f"За {des_value} {des_first} ви отримаєте {'{:.2f}'.format(convert_)} {des_second}")
    return True


def convert_start():
    valuta = []
    back_day = datetime
    for i in range(today_date.day):
        back_day = today_date - timedelta(days=i+1)
        r_to_date = requests.get(
            "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + back_day.strftime('%d.%m.%Y'))
        json_ex_rate = r_to_date.json()
        list_old_rate = json_ex_rate['exchangeRate']
        del list_old_rate[0]
        for item in list_old_rate:
            if 'currency' in item:
                print(f"- {item['currency']} ")
                valuta.append(item['currency'])
            else:
                continue
        break
    print(back_day.strftime('%d.%m.%Y'))
    if convert(valuta, back_day):
        return True
    else:
        print('errrrrrr')
        return True
