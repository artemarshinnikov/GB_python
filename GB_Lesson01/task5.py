# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
proceeds = int(input("Введите выручку >>>"))
costs = int(input("Введите издержки >>>"))
if proceeds > costs:
    print("Фирма получает прибыль")
    print("Рентабельность выручки данной фирмы -", ((proceeds - costs) / proceeds) * 100, "%")
    staff = int(input("Введите количество персонала >>>"))
    print("Каждый сотрудник фирмы получает -", (proceeds - costs) / staff)
else:
    print("Фирма работает в убыток")