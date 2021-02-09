my_list = [20, 50, 120, 200]
for value in my_list:
    if value > 100:
        print(value)
#######################
my_list = [20, 50, 120, 200]
result = []
for value in my_list:
    if value > 100:
        result.append(value)
print(result)
########################

my_list = [20, 50, 120, 200]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
if len(my_list) >= 2:
    my_list.append(my_list[-1]+my_list[-2])
    print(my_list)
#########################
value = input("Введите число:")
if value.isdigit():
    value = float(value)
    result = value ** -1
else:
    print("не верный ввод")
    result = ""
try:
    value=float(value)
    result = value ** -1
except (ValueError, TypeError):
    print("Не верный ввод")
    value = 0
    result = 1
print(result)
##############
# my_list = [20, 50, 120, 200]
# my_results = []
# for index in my_list:
#     if index % 2 == 0:
#         my_results.append(index)
#         print(my_results)
