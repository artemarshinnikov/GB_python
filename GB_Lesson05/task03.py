# 3. Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

my_file = open('task03.txt', 'r')
my_list = my_file.readlines()
poor = []
salary = []
for i in my_list:
    i = i.split()
    if float(i[1]) < 20000:
        poor.append(i[0])
    salary.append(i[1])
print(f'Оклад меньше 20000 у {poor}, средний оклад {sum(map(float, salary)) / len(salary)}')
