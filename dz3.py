value1 = int(input("Введите число:"))
new_value1 = value1 / 2 if value1 < 100 else (-value1)
print(new_value1)
##############################
value2 = int(input("Введите число:"))
new_value2 = 1 if value2 < 100 else 0
print(new_value2)
##############################
value3 = int(input("Введите число:"))
new_value3 = True if value3 < 100 else False
print(new_value3)
###############################
my_str1 = str(input("Введите строку:"))
print(my_str1.upper())
##############################
my_str2 = str(input("Введите строку:"))
print(my_str2.lower())
###############################
my_str3 = str(input("Введите строку:"))
my_str3 = my_str3 + my_str3 if len(my_str3) < 5 else my_str3
print(my_str3)
###############################
my_str4 = str(input("Введите строку:"))
my_str4 = my_str4 + my_str4[::-1] if len(my_str4) < 5 else my_str4
print(my_str4)

