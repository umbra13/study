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





##################################
# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список
my_str = "abcde"

print('' if (my_str := input() + '_') else '', [my_str[index:index+2] for index in range(0, len(my_str) // 2 * 2, 2)], sep='')

###################################
# 8 ?

# 9 ?

# 10 ?

