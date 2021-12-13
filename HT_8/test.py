dict_nominal = {"10":10,"20":10,"50":10,"100":10,"200":10,"500":10,"1000":10}
nominals = ["1000","500","200","100","50","20","10"]
amount = 110
print(dict_nominal)

for key in range(len(nominals)):
    if int(nominals[key]) <= amount and dict_nominal[nominals[key]] > 0:
        while amount % 20 == 10 and amount !=0:
            dict_nominal["50"] -= 1
            amount -= 50
        while amount > int(nominals[key]) == 0 and amount !=0:
            dict_nominal[nominals[key]] -= 1
            amount -= int(nominals[key])
        
print(dict_nominal)