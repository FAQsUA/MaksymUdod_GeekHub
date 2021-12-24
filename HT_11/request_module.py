import requests
import random


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


def take_full_inf_request(user_id):
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    json_r = r.json()
    info_dict = json_r[user_id - 1]
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


def posts(user_id):
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    json_r = r.json()
    post_list = []
    post_count = 0
    for _dict in range(len(json_r)):
        if json_r[_dict]['userId'] == user_id:
            post_count += 1
            post_dict = {}
            for key, value in json_r[_dict].items():

                if key == 'id':
                    post_dict.update({key: value})
                    continue
                elif key == 'title':
                    post_dict.update({key: value})
                    continue

            post_list.append(post_dict)

    print(f' Кількість постів: {post_count}')
    for _dict in range(len(post_list)):
        print(f' id: {post_list[_dict]["id"]}\n Заголовок: {post_list[_dict]["title"]}')


def post(user_id, des):
    r_post = requests.get('https://jsonplaceholder.typicode.com/posts?userId=' + str(user_id) + '&id=' + str(des))
    json_r_post = r_post.json()

    if r_post.content == b'[]':
        print('Не вірний ID !!!')
        return False
    else:
        r_comm = requests.get('https://jsonplaceholder.typicode.com/comments?postId=' + str(des))
        json_r_comm = r_comm.json()

        print(f'id = {json_r_post[0]["userId"]}\nЗаголовок: {json_r_post[0]["title"]}\nТекст:\n{json_r_post[0]["body"].strip()}\n' \
              f'Кількість коментарів: {len(json_r_comm)}\nid comments:')
        for item in range(len(json_r_comm)):
            print(f'{json_r_comm[item]["id"]}', end=',')
        print()
        return True


def todo(user_id, tru_false):
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    json_r = r.json()
    todo_list_true = []
    todo_list_false = []
    for _dict in range(len(json_r)):
        if json_r[_dict]['userId'] == user_id:
            if json_r[_dict]['completed']:
                todo_list_true.append(json_r[_dict]['title'])
                continue
            else:
                todo_list_false.append(json_r[_dict]['title'])
                continue
    if tru_false:
        for item in todo_list_true:
            print(f' - {item}')
    else:
        for item in todo_list_false:
            print(f' - {item}')


def random_img():
    img_id = random.randint(1, 5000)

    r = requests.get("https://jsonplaceholder.typicode.com/photos")
    json_r = r.json()

    for _dict in range(len(json_r)):
        if json_r[_dict]['id'] == img_id:
            return json_r[_dict]['url']
        else:
            continue
