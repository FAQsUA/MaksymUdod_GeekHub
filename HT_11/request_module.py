import requests


def take_short_inf_request():
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    json_r = r.json()

    dict_list = []

    for item in range(len(json_r)):
        new_dict = {}

        new_dict.update({'id': json_r[item]['id']})
        new_dict.update({'name': json_r[item]['name']})
        new_dict.update({'username': json_r[item]['username']})

        dict_list.append(new_dict)
        del new_dict

    return dict_list


def print_dict(dict_):
    print(' >>> Address <<< ')
    for key, value in dict_.items():
        if key == 'geo':
            break
        else:
            print(f'{key}: {value}')


def sort_json(user_id):
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    json_r = r.json()

    for _dict in json_r:
        for key, value in _dict.items():
            if key != 'address' and key != 'company':
                print(f'{key}: {value}')
            else:
                if key == 'address':
                    print_dict(value)
                elif key == 'company':
                    print_dict(value)
                '''
                      for key_a, value_a in address_dict.items():
                          if key_a != 'geo':
                              print(f'{key_a} : {value_a}')
                          else:
                              geo_dict = value_a
                              continue

                      print('>>> Geo <<<')
                      for key_g, value_g in geo_dict.items():
                          print(f'{key_g} : {value_g}')

                      print('>>> Company <<<')
                      for key_c, value_c in company_dict.items():
                          print(f'{key_c} : {value_c}')
                  
                
            else:
                if key == 'address':
                    address_dict = value
                    continue
                elif key == 'company':
                    company_dict = value
                    continue
    return info_dict, address_dict, geo_dict, company_dict'''


def take_full_inf_request(user_id):
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    json_r = r.json()
    info_dict = json_r[user_id-1]
    address_dict, company_dict = {}, {}
    print('\n >>> INFO <<< ')
    for key, value in info_dict.items():
        if key == 'address':
            address_dict = value
            continue
        elif key == 'company':
            company_dict = value
            continue
        else:
            print(f' {key}: {value} ')
    print('\n >>> ADDRESS <<< ')
    for key, value in address_dict.items():
        if key == 'geo':
            continue
        else:
            print(f' {key}: {value} ')

    print('\n >>> COMPANY <<< ')
    for key, value in company_dict.items():
        print(f' {key}: {value} ')
    print()

