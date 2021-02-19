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
#############
my_list = [20, 50, 120, 200]
my_results = []
for index, number in enumerate(my_list):
    my_list[index] = number + index+1
    if my_list[index] % 2 == 0:
        my_results.append(my_list[index])
        print(my_results)

##############

my_list_1 = [1, 2, 3, 4]
my_list_2 = [5, 6, 7, 8]
for index_1 in enumerate(my_list_1):
      for index_2 in enumerate(my_list_2):
        print(index_1 + index_2)

###################

my_string = '0123456789'
my_list = [int(index) for index in my_string if '0' <= index <= '9']
print(my_list)
