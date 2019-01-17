# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
def transpose(matrix):
    return list(map(list, zip(*matrix)))

print(transpose(matrix))

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

from functools import reduce
def mult(num_string):
    list_of_ints = map(lambda x: int(x), list(num_string.replace('\n','')))
    return reduce(lambda x, y: x * y, list_of_ints)

def find_largest_sequence(num_string):
    current_pos, current_max = 0, 0
    for i in range(len(num_string) - 6):
        string = num_string[i:(i+6)]
        result = mult(string)
        if result > current_max:
            current_max = result
            current_pos = i
    return (current_max, current_pos)

print(find_largest_sequence(number))

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

from random import randint
def generate_queen():
    return (randint(1,8), randint(1,8))

def generate_queens_set():
    queens = set()
    while len(queens) < 8: 
        queens.update([generate_queen()])
    return queens

def calculate_threatened_squares(queen_position):
    '''
    Возвращает множество кортежей, куда может сходить ферзь
    '''
    x, y = queen_position
    squares = set()
    # добавляем клетки по вертикали и горизонтали
    squares.update([(x, i+1) for i in range(0,7)])
    squares.update([(i+1, y) for i in range(0,7)])
    
    # добавляем клетки по диагоналям
    for dir_shift in [[1,1], [-1,1], [1, -1], [-1,-1]]:
        x_sq, y_sq = x, y
        while True:
            x_sq += dir_shift[0]
            y_sq += dir_shift[1]
            if x_sq < 0 or x_sq > 8 or y_sq < 0 or y_sq > 8:
                break
            new_position = (x_sq, y_sq)
            squares.update([new_position])    
    return squares

def queen_battle():
    queens = generate_queens_set()
    for queen in queens:
        other_queens = queens - set(queen)
        threatened_squares = calculate_threatened_squares(queen)
        if other_queens.intersection(threatened_squares):
            return True
    return False

result = queen_battle()
print("YES") if result else print("NO")