def get_money(money):

    dict_nominal = {"10":5,"20":5,"50":2,"100":0,"200":5,"500":5,"1000":5}
    res = []
    summa = 0
    for key, value in sorted(dict_nominal.items(), key=lambda x: -int(x[0])):
        while summa + int(key) <= money and dict_nominal[key] > 0:
            summa += int(key)
            dict_nominal[key] -= 1
            res.append(key)
    print(dict_nominal)
    return res
 
 
print(get_money(160))