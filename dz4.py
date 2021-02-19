# У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [20, 50, 120, 200]
for value in my_list:
    if value > 100:
        print(value)
#######################

# У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [20, 50, 120, 200]
result = []
for value in my_list:
    if value > 100:
        result.append(value)
print(result)
########################
# У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [20, 50, 120, 200]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
if len(my_list) >= 2:
    my_list.append(my_list[-1]+my_list[-2])
    print(my_list)
#########################

#  Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.

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

# У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения из my_list для которых сумма индекса и значения будет четной.

my_list = [20, 50, 120, 200]
my_results = []
for index, number in enumerate(my_list):
    my_list[index] = number + index+1
    if my_list[index] % 2 == 0:
        my_results.append(my_list[index])
        print(my_results)

##############
#  У вас есть два списка my_list_1 и my_list_2 равной длинны.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу (можно range, можно enumerate).

my_list_1 = [1, 2, 3, 4]
my_list_2 = [5, 6, 7, 8]
for index_1 in enumerate(my_list_1):
      for index_2 in enumerate(my_list_2):
        print(index_1 + index_2)

###################
# У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.

my_string = '0123456789'
my_list = [int(index) for index in my_string if '0' <= index <= '9']
print(my_list)
