""" 1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
   Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
   пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;) """


import selectors
import requests
import lxml
from bs4 import BeautifulSoup as bs


main_dict = {}


def author_on_page(sup):
    name = sup.select('h3.author-title')[0].text.strip()
    born_date = sup.select('span.author-born-date')[0].text.strip()
    born_location = sup.select('span.author-born-location')[0].text.strip()
    text = [sup.select('div.author-description')[0].text.strip()]
    _dict = {'born-date': born_date, 'born-location': born_location, 'description': text}
    __dict = {name: _dict}

    print(name)

    if not main_dict:
        main_dict.update(__dict)
        return None
    else:
        if name in main_dict:
            help_list = main_dict[name]['description']
            help_list.append(text[0])
            main_dict[name]['description'] = help_list
        else:
            main_dict.update(__dict)


def all_author_on_page(sup):
    for author in sup.select('.quote span a:link'):
        r_about = requests.get("http://quotes.toscrape.com" + author['href'])
        soup_author = bs(r_about.text, 'lxml')
        author_on_page(soup_author)
    return True


def pages():
    page = ''
    page__ = '/page/'
    page_count = 1
    while True:
        page_count += 1
        r = requests.get("http://quotes.toscrape.com/" + page)
        soup = bs(r.text, 'lxml')
        if all_author_on_page(soup):
            if soup.select('li.next a:link'):
                page = page__ + str(page_count)
            else:
                break


pages()

for k,v in main_dict.items():
    print(k,v)
