# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
int_var1 = 5
int_var2 = 2
int_var3 = int_var1 + int_var2
print(f"числовая переменная 1 = {int_var1}, числовая переменная 2 = {int_var2}, числовая переменная 3 = {int_var3}")
str_var1 = "Hello"
str_var2 = "world"
str_var3 = str_var1 + str_var2
print("строковая переменная 1 =", str_var1, "строковая переменная 2 =", str_var2, "строковая переменная 3 =", str_var3)
str_var1 = input("Введите строку >>>")
str_var2 = "TEST " + str_var1
print(f"строковая переменная 1 = {str_var1}, строковая переменная 2 = {str_var2}")
int_var1 = int(input("Введите число >>>"))
int_var2 = 1 + int_var1
print("числовая переменная 1 =", int_var1, "числовая переменная 2 =", int_var2)
