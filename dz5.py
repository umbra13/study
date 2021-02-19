# Дано целое число (int). Определить сколько нулей в этом числе

# number = 11020
# number = str(number)
# print(number.count('0'))
# print(input().count('0'))
###################

#Дано целое число (int). Определить сколько нулей в конце этого числа

# number = 50760700
# count = 0
# while number % 10 == 0:
#     count += 1
#     number //= 10
# print(count)
##################
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
for index_1 in range(len(my_list_1)):
    for index_2 in range(len(my_list_2)):
        print(index_1 + index_2)


##########################
# Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.


# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 15, 20, 25]
# my_result = [my_list_1[i] for i in range(len(my_list_1)) if my_list_1[i] % 2 == 0] + [my_list_2[i] for i in range(len(my_list_2)) if my_list_2[i] % 2 == 1]
# print(my_result)

##################
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте

