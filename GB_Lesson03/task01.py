# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(arg1, arg2):
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Ошибка. Делитель не может быть равен 0.")


dividend = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))
print(div(dividend, divider))
