# Дано целое число (int). Определить сколько нулей в этом числе

number = 11020
number = str(number)
print(number.count('0'))
print(input().count('0'))
##################

#Дано целое число (int). Определить сколько нулей в конце этого числа

number = 50760700
count = 0
while number % 10 == 0:
    count += 1
    number //= 10
print(count)
##################
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
result = []
result += my_list_1[::2]
result += my_list_2[1::2]
print(result)

##########################
# Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.


my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = [my_list_1[i] for i in range(len(my_list_1)) if my_list_1[i] % 2 == 0] + [my_list_2[i] for i in range(len(my_list_2)) if my_list_2[i] % 2 == 1]
print(my_result)

##################
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте

my_list = [1, 2, 3, 4, 5]
new_list = []
my_list.pop(0)
new_list.extend(my_list)
new_list.append(1)
print(new_list)

###############################
# Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.

my_list = [1, 2, 3, 4, 5]
my_list.pop(0)
my_list.append(1)
print(my_list)

########################################
# Дана строка в которой есть числа (разделяются пробелами). Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.

my_str = "43 больше чем 34 но меньше чем 56"
my_list = my_str.split()
result = 0
for item in my_list:
    if item.isdigit():
        result += int(item)
print(result)

##################################
# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список
my_str = 'abcd'
if len(my_str) % 2 != 0:
    my_str += "_"
index = 0
result_list = []
step = 0
while index < len(my_str) / 2:
    result_list.append(my_str[step:step+2])
    step += 2
    index += 1
print(result_list)

###################################
# 8 Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

my_str = "my_long str"
l_limit = "o"
r_limit = "t"
l_index = my_str.index(l_limit)
r_index = my_str.index(r_limit)
sub_str = my_str[l_index + 1:r_index]
print(sub_str)

# 9 Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
l_index = my_str.index(l_limit)
r_index = my_str.rindex(r_limit)
sub_str = my_str[l_index + 1:r_index]
print(sub_str)

# 10 Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
my_list = [2, 4, 5, 3, 0, 7]
counter = 0
if len(my_list) >= 3:
    index = 0
    pos = 1
    while index < len(my_list) - 2:
        if my_list[pos] > my_list[pos - 1] + my_list[pos + 1]:
            counter += 1
        index += 1
        pos += 1

print(counter)
