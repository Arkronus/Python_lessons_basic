# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker():
    def __init__(self, hours_line, workers_line):
        self.salary, self.norm_hours = self._parse_workers_line(workers_line)
        self.work_hours = self._parse_hours_line(hours_line) 

    def _parse_workers_line(self, line):
        salary = int(line[21:27])
        norm_hours = int(line[52:].strip())
        return salary, norm_hours

    def _parse_hours_line(self, line):
        work_hours = int(line[22:])
        return work_hours

    def calc_line_salary(self):
        mod_salary = 0
        if self.work_hours <= self.norm_hours:
            mod_salary = self.salary * (self.work_hours / self.norm_hours)
        else:
            extra_hours = (self.work_hours - self.norm_hours) * 2
            mod_salary = self.salary * (1 + (extra_hours / self.norm_hours))
        return round(mod_salary, 2)

class SalaryCalculator():
    def __init__(self, hours_of_path, workers_path):
        self.hours_data = self.read_data(hours_of_path)
        self.workers_data = self.read_data(workers_path)
        

    def calculate_salary(self):
        workers_salary = []
        for worker_name in self.get_worker_names():
            worker = Worker(self.workers_data[worker_name], self.hours_data[worker_name])
            workers_salary.append({'name': worker_name, 'result':worker.calc_line_salary()})
        return workers_salary

    def read_data(self, fname):
        with open(os.path.join('data', fname), 'r', encoding='UTF-8') as f:
            datastr = f.readlines()[1:]
        data = {}
        for line in datastr:

            name = line[:20].strip()
            name = ' '.join(name.split())
            data[name] = line
        return data


    def get_worker_names(self):
        return list(self.workers_data.keys())

calc = SalaryCalculator('workers','hours_of')
salary = calc.calculate_salary()

print(salary)