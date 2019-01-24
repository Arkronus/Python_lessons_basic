# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class Triangle():
    def __init__(self,a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._ab = self._side_length(a, b)
        self._ac = self._side_length(a, c)
        self._bc = self._side_length(b, c)

    def _side_length(self,a, b):
        return round(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 2)

    def area(self):
        """Расчет площади треугольника по формуле Герона"""
        s = (self._ab + self._ac + self._bc) / 2
        area = math.sqrt(s * (s - self._ab) * (s - self._ac)* (s - self._bc))
        return round(area, 2)

    def heights(self):
        """Возвращает массив высот треугольника"""
        return[round(self.area() / base, 2) 
            for base in [self._ab, self._ac, self._bc]]

    def perimeter(self):
        return round(self._ac + self._ab + self._bc, 2)



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze():
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._ab = self._side_length(a, b)
        self._ac = self._side_length(a, c)
        self._bc = self._side_length(b, c)
        self._cd = self._side_length(c, d)

    def _side_length(self,a, b):
        return round(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 2)

    def sides():
        return [self._ab, self._ac, self._bc, self._cd]

    def perimeter(self):
        return round(sum(self.sides()), 2)

if __name__ == '__main__':
    tr = Triangle([0,0], [3, 6], [6,6])
    print(tr.area())
    print(tr.heights())
    print(tr.perimeter())

