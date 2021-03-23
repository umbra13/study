# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.


import requests
import csv

url = "http://api.forismatic.com/api/1.0/"


def get_quotes(count):
    quotes_list = []
    index = 0

    while index < count:
        params = {"method": "getQuote",
                  "format": "json",
                  "key": index,
                  "lang": "ru"}
        responce = requests.get(url, params=params)
        data = responce.json()
        if data["quoteAuthor"] != "":
            index += 1
            quotes_list.append(data)
    return quotes_list


# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
def sort_key_by_author(obj_dict):
    return obj_dict["quoteAuthor"]


def create_file(count, filename="fail.csv"):
    quotes_list = get_quotes(count)
    quotes_list = sorted(quotes_list, key=sort_key_by_author)
    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Athor", "Quote", "URL"])
        for quote in quotes_list:
            filewriter.writerow([quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"]])

create_file(5)