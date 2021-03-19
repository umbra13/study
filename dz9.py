import json
import random
import os

def read_txt_file(filename):
    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    return data
f = read_txt_file("names.txt")
names_list = []
for line in f:
    line_list = line.split(chr(9))
    names_list.append(line_list[1])
print(names_list)

###########################


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



def create_dict():
    len = create_point(5, 20)
    result_dict = {}
    index = 0
    while index < len:
        key = create_str(5, 5)
        while key in result_dict:
            key = create_str(5, 5)

        value_type = create_point(0, 2)
        if value_type == 0:
            value = create_point(-100, 100)
        if value_type == 1:
            value = random.uniform(0, 1)
        if value_type == 2:
            value = bool(create_point(0, 1))
        result_dict[key] = value
        index += 1
    return result_dict

def generate_and_write_json(filename):
    f = open(filename, "w")
    json.dump(create_dict(), f)

generate_and_write_json("qwe.json")