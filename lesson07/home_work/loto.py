#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import os
import sys
import itertools

NUM_ROWS = 3
NUM_COLUMNS = 5

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class BagOfNumbers():

    def __init__(self, start, stop):
        numbers = [i for i in range(start, stop+1)]
        random.shuffle(numbers)
        self._numbers = numbers
        self.size = len(numbers)

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return self

    def __next__(self):
        if len(self._numbers)>0:
            self.size -= 1
            return self._numbers.pop()
        else:
            raise StopIteration

class Number():
    def __init__(self, value):
        self.value = value
        self.checked = False

    def __str__(self):
        if self.checked:
            return '--'
        else:
            return "{:02d}".format(self.value)
        
class LotoBoard():
    def __init__(self, numbers):
        self.numbers = numbers


    def __str__(self):
        board_string = ''
        board_string += '---'*5 + "\n"
        for row in self.numbers:
            string_row = map(lambda x: str(x), row)
            board_string += '|'.join(string_row) + "\n"
        board_string += '---'*5 + "\n"
        return board_string


    def has_value(self, value):
        for num in self._flatten_list():
            if num.value == value: return True
        return False


    def mark_value(self, value):
        for num in self._flatten_list():
            if num.value == value: num.checked = True


    def _flatten_list(self):
        return list(itertools.chain(*self.numbers))


    def all_numbers_checked(self):
        return all( map(lambda x: x.checked, self._flatten_list()))

class LotoGenerator():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.numbers = self._generate_numbers(NUM_ROWS, NUM_COLUMNS)

    def _generate_numbers(self, num_rows, num_columns):
        numbers = set([i for i in range(self.start, self.stop+1)])
        numbers_array = []
        for i in range(num_rows):
            line_numbers = set(random.sample(numbers, num_columns))
            numbers -= line_numbers
            line_numbers = list(map(lambda x: Number(x), sorted(list(line_numbers))))
            numbers_array.append(line_numbers)
        return numbers_array

class Game():

    def __init__(self, player_board, computer_board, bag):
        self._player_board = player_board
        self._computer_board = computer_board
        self._bag = bag

    def start_game(self):

        for num in self._bag:
            cls()

            # проверяем, есть ли выигравшая доска
            self._check_boards()

            print("Новый бочонок: {:02d}. Осталось {} бочонков".format(num, self._bag.size))
            print("------ Ваша карточка -----")
            print(self._player_board)

            print("-- Карточка компьютера ---")
            print(self._computer_board)
            answer = ''
            while answer not in ('y', 'n'):
                answer = input("Зачеркнуть цифру? (y/n):")

                # проверяем ход игрока
                if answer == 'y':
                    if self._player_board.has_value(num):
                        self._player_board.mark_value(num)
                    else:
                       print("Вы отказались, а зря! У вас был такой номер! Игра окончена.") 
                       sys.exit()

            # ход компьютера
            if self._computer_board.has_value(num):
                self._computer_board.mark_value(num)

    def _check_boards(self):
        if self._player_board.all_numbers_checked():
            print("Игрок выиграл!")
            sys.exit()
        elif self._computer_board.all_numbers_checked():
            print("Компьютер выиграл!")
            sys.exit()

if __name__ == '__main__':
    MIN = 1
    MAX = 99
    player_board = LotoBoard(LotoGenerator(MIN,MAX).numbers)
    computer_board = LotoBoard(LotoGenerator(MIN,MAX).numbers)
    bag = BagOfNumbers(MIN,MAX)
    game = Game(player_board, computer_board, bag)
    game.start_game()