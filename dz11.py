import json
import re



def read_json_file(filename):
    with open(filename, "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def sort_key_by_name(obj_dict):
    name = obj_dict["name"]
    name_list = name.split(" ")
    return name_list[-1]

print( sorted(read_json_file("data.json"),key=sort_key_by_name) )

def sort_key_by_year(obj_dict):
    years = obj_dict["years"]
    dates = re.findall("[0-9]+", years)
    return int(dates[-1])
print( sorted(read_json_file("data.json"),key=sort_key_by_year) )

def sort_key_by_text(obj_dict):
     return len(obj_dict["text"])
print( sorted(read_json_file("data.json"),key=sort_key_by_text) )