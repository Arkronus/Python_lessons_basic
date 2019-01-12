# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

from fractions import Fraction

def parse(input_string):
    if ' + ' in input_string:
        input_array = input_string.split(' + ')
        summation = True
    elif ' - ' in input_string:
        input_array = input_string.split(' - ')
        summation = False
    else:
        raise ValueError('Неправильая дробь')
    if summation:
        result = Fraction(input_array[0]) + Fraction(input_array[1])
    else:
        result = Fraction(input_array[0]) - Fraction(input_array[1])
    return result

def ex1():
    test_inputs = ["5/6 + 4/7", "-2/3 - -2"]
    for i in test_inputs:
        print(parse(i))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

workers_data = []
hours_data = []

import os

def parse_workers_line(line):
    data = {}
    fname = line[:8].strip() + " " + line[8:21].strip()
    salary = int(line[21:27])
    norm_hours = int(line[52:])
    data[fname] = {'salary': salary, 'norm_hours': norm_hours}
    return data

def parse_hours_line(line):
    data = {}
    fname = line[:8].strip() + " " + line[8:21].strip()
    work_hours = int(line[22:])
    data[fname] = work_hours
    return data

def array_to_dict(array):
    data = {}
    for val in array:
        name = list(val.keys())[0]
        values = list(val.values())[0]
        data[name] = values  
    return data

def read_data(fname, parser_func):
    with open(os.path.join('data', fname), 'r', encoding='UTF-8') as f:
        data = f.readlines()
    data = data[1:] # удаляем шапку
    parsed_data = list(map(parser_func, data))
    return parsed_data

def calc_line_salary(salary, norm_hours, actual_hours):
    mod_salary = 0
    if actual_hours <= norm_hours:
        mod_salary = salary * (actual_hours / norm_hours)
    else:
        extra_hours = (actual_hours - norm_hours) * 2
        mod_salary = salary * (1 + (extra_hours / norm_hours))
    return round(mod_salary, 2)

# print(calc_line_salary(22000, 140, 120))    

def calc_salary(workers_data, hours_data):
    salary_data = {}
    for name in workers_data:
        salary_data[name] = calc_line_salary( workers_data[name]['salary'], workers_data[name]['norm_hours'], hours_data[name] )
    return salary_data

def ex2():
    workers_data = array_to_dict(read_data('workers', parse_workers_line))
    hours_data = array_to_dict(read_data('hours_of', parse_hours_line))
    result = calc_salary(workers_data, hours_data)
    print(result)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

RUS_CHARS = list(map(chr, range(ord('А'), ord('Я')+1)))

def get_fruits_data():
    with open(os.path.join('data', 'fruits.txt'), 'r', encoding='UTF-8') as f:
        return [line.strip() for line in f.readlines() if len(line)>1]

def ex3():
    fruits_data = get_fruits_data()
    fruits_dict = { letter:[] for letter in RUS_CHARS } 
    for fruit in fruits_data:
        first_letter = fruit[0]
        fruits_dict[first_letter].append(fruit)

    for k in fruits_dict:
        filename = "fruits_" + k
        with open(os.path.join('data', filename), 'w', encoding='UTF-8') as f:
            for fruit in fruits_dict[k]:
                f.write("%s\n" % fruit)



if __name__ == '__main__':
    ex1()
    ex2()
    ex3()