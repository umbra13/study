#####1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
#Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.


import random

def create_point(min_limit, max_limit):
    point = random.randint(min_limit, max_limit)
    return point

def create_str(min_limit, max_limit):
    len = create_point(min_limit, max_limit)
    str = ""
    index = 0
    while index < len:
        str += chr(create_point(97, 122)) # ascii table
        index += 1
    return str

###########################################################################################
#
#  Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# Обязательные параметры функции: names и domains.
# Параметры по умолчанию: границы генерируемого числа (100, 999), границы генерируемой строки (5, 7)
#
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться.

def create_email(domains, names, min_num = 100 , max_num = 999, min_len = 5 , max_len = 7):
    result = names[create_point(0, len(names)-1)] + "."
    result += str(create_point(min_num, max_num)) + "@"
    result += create_str(min_len, max_len) + "."
    result += domains[create_point(0, len(domains)-1)]
    return result

names = ["klon", "milk", "beer"]
domains = ["to", "ru", "pro"]
e_mail = create_email(domains, names)
print(e_mail)
