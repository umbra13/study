import random
# Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.

my_list = []
def create_point(min_limit, max_limit):
    point = random.randint(min_limit, max_limit)
    return point
for index in range(0, 20):
    my_list.append(create_point(0, 100))

print(my_list)
############################################
# Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси

def create_point(x,y):
    point = (random.randint(x, y), random.randint(x, y))
    return point

triangle = {"A": create_point(-10, 10,),
            "B": create_point(-10, 10),
            "C": create_point(-10, 10)}
print(triangle)

#################################
#Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.

def my_print(str):
    print("***" + str + "***")
my_print("I'm the string")

##################################
#  Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.


persons = [{"name": "John", "age": 15},
          {"name": "Jack", "age": 45},
          {"name": "Marks", "age": 34},
          {"name": "Tom", "age": 15},
           {"name": "maxim", "age": 13}]
min_age = persons[0]["age"]
max_name_len = len(persons[0]["name"])
youngs_list = []
name_len_list = []
sum_age = 0
for person in persons:
    if person["age"] == min_age:
        youngs_list.append(person["name"])
    if person["age"] < min_age:
        min_age = person["age"]
        youngs_list.clear()
        youngs_list.append(person["name"])

    if len(person["name"]) == max_name_len:
        name_len_list.append(person["name"])
    if len(person["name"]) > max_name_len:
        max_name_len = len(person["name"])
        name_len_list.clear()
        name_len_list.append(person["name"])

    sum_age += person["age"]

print(youngs_list)
print(name_len_list)
print(sum_age / len(persons))

#################################
# Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {1: 1,
             2: 2,
             3: 3}
my_dict_2 = {5: 4,
             2: 6,
             4: 3}

my_dict_keys_1 = my_dict_1.keys()
my_dict_keys_2 = my_dict_2.keys()
unique_dict = {}
same_key_list = []
unique_1 = []
result_dict = my_dict_2.copy()
for a in my_dict_keys_1:
    counter = 0
    for b in my_dict_keys_2:
        if a == b:
            same_key_list.append(a)
            counter += 1
    if counter == 0:
        unique_1.append(a)
        unique_dict[a] = my_dict_1[a]
        result_dict[a] = my_dict_1[a]
    else:
        value = my_dict_1[a]
        result_dict[a] = [value, result_dict[a]]

print(same_key_list)
print(unique_1)
print(unique_dict)
print(result_dict)
