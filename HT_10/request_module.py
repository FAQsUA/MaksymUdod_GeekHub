from datetime import datetime
from time import sleep
import requests


take_date = datetime.now()
today_date = take_date.strftime('%d.%m.%Y')
year = int(take_date.year)


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


def do_cur_request_2(des):
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

    difference = float(dict_ex_rate['saleRateNB']) - float(do_cur_request_2(des))

    print(f"Дата: {date} \nКурс НБУ: {dict_ex_rate['saleRateNB']} {float('{0:.4f}'.format(difference))}")

    return True


def start():
    while True:
        try:
            date_input = input('Введіть дату (дд.мм.рррр) --> ')

            if int(date_input[0:2]) <= 31:
                if int(date_input[3:5]) <= 12:
                    if int(date_input[6:]) <= int(year):
                        if date_input == today_date:
                            do_cur_request(valute_des())
                            break
                        else:
                            do_request(valute_des(), date_input)
                            break
                    else:
                        print('Error, input correct date')
                        continue

        except ValueError:
            print('Error, input correct date')
            continue
        except:
            print("errr")
            continue

    return True
