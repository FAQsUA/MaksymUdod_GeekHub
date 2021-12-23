from datetime import datetime
import datetime
import requests
import time

take_date_and_time = datetime.datetime.now()
today_date = take_date_and_time.strftime('%d.%m.%Y')
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


def do_cur_request(des):
    r_to_cur_date = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    json_cur_ex_rate = r_to_cur_date.json()

    dict_cur_ex_rate = {}
    for item in json_cur_ex_rate:
        if des == 1:
            if item['ccy'] == 'USD':
                dict_cur_ex_rate = item
                break
        elif des == 2:
            if item['ccy'] == 'EUR':
                dict_cur_ex_rate = item
                break
    print(f"Дата: {today_date} \nКурс : {dict_cur_ex_rate['sale']} --------")

    return dict_cur_ex_rate['sale']


def do_cur_request_for_inside(des, *args):
    r_to_cur_date = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    json_cur_ex_rate = r_to_cur_date.json()

    dict_cur_ex_rate = {}
    for item in json_cur_ex_rate:
        if des == 1:
            if item['ccy'] == 'USD':
                dict_cur_ex_rate = item
                break
        elif des == 2:
            if item['ccy'] == 'EUR':
                dict_cur_ex_rate = item
                break

    return dict_cur_ex_rate['sale']


def do_request(des, date):
    r_to_date = requests.get("https://api.privatbank.ua/p24api/exchange_rates?json&date=" + date)
    json_ex_rate = r_to_date.json()
    list_ex_rate = json_ex_rate['exchangeRate']
    del list_ex_rate[0]

    dict_ex_rate = {}

    for item in list_ex_rate:
        if des == 1:
            if item['currency'] == 'USD':
                dict_ex_rate = item
                break
        elif des == 2:
            if item['currency'] == 'EUR':
                dict_ex_rate = item
                break

    difference = float(dict_ex_rate['saleRateNB']) - float(do_cur_request_for_inside(des))

    print(f"Дата: {date} \nКурс НБУ: {dict_ex_rate['saleRateNB']} {float('{0:.4f}'.format(difference))}")

    return True


def rate_start():
    while True:
        try:
            date_input = input('Введіть дату (дд.мм.рррр) --> ')

            if date_input > today_date:
                print('Error, input correct date')
                continue
            elif date_input == today_date:
                do_cur_request(valute_des())
                break
            else:
                do_request(valute_des(), date_input)
                break

        except ValueError:
            print('Error, input correct date')
            continue

    return True


def convert():
    valuta = ['UAH', 'USD', 'EUR']
    convert_ = 0
    flag = True
    while flag:
        try:
            des_first = input('Виберіть першу валюту (UAH / USD / EUR) --> ')
            if des_first in valuta:
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
                    des_second = input('Виберіть другу валюту (UAH / USD / EUR) --> ')
                    if des_second in valuta:
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

    r_to_cur_date = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    json_cur_ex_rate = r_to_cur_date.json()

    for item in json_cur_ex_rate:
        if des_first == 'UAH':
            if item['ccy'] == des_second:
                convert_ = float(des_value) / float(item['sale'])
                break
        elif des_first == 'USD':
            if des_second != 'UAH':
                if item['ccy'] == des_first:
                    convert_ = (float(des_value) * float(item['sale'])) \
                               / float(json_cur_ex_rate[1]['sale'])
                    break
            else:
                if item['ccy'] == des_first:
                    convert_ = float(des_value) * float(item['sale'])

        elif des_first == 'EUR':
            if des_second != 'UAH':
                if item['ccy'] == des_first:
                    convert_ = (float(des_value) * float(item['sale'])) \
                               / float(json_cur_ex_rate[0]['sale'])
                    break
            else:
                if item['ccy'] == des_first:
                    convert_ = float(des_value) * float(item['sale'])

    print(f"За {des_value} {des_first} ви отримаєте {'{:.2f}'.format(convert_)} {des_second}")
    return True
