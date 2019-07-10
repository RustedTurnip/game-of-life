#!/usr/bin/env python3
from random import randint
import time
import os

class Board:
    _chars = [' ', bytes((219,)).decode('cp437')]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.one_distribution = 0.5

    def set_up(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                rand = float(randint(1, 10))/10.0
                row.append(1) if rand < self.one_distribution else row.append(0)
            self.grid.append(row)

    def new_generation(self):
        new_board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                val = self.calculate_population((i, j))
                row.append(self.calculate_cell(self.grid[i][j], val))
            new_board.append(row)
        self.grid = new_board

    def calculate_cell(self, current, value):
        if value == 3:
            return 1
        elif current == 1 and (value == 2 or value == 3):
            return 1
        return 0

    def calculate_population(self, coords):
        val = 0 - self.grid[coords[0]][coords[1]]
        count_range = [3, 3]
        start = [coords[0] - 1, coords[1] - 1]

        if coords[0] == 0:
            start[0] += 1
            count_range[0] -= 1
        if coords[1] == 0:
            start[1] += 1
            count_range[1] -= 1
        if coords[0] == self.height - 1:
            count_range[0] -= 1
        if coords[1] == self.width - 1:
            count_range[1] -= 1

        for i in range(count_range[0]):
            for j in range(count_range[1]):
                x, y = i + start[0], j + start[1]
                val += self.grid[x][y]
        return val

    def __str__(self):
        string = ''
        for r in self.grid:
            for c in r:
                string += Board._chars[c]
            string += '\n'
        return string[:-1]


def main_test():
    os.system('cls' if os.name == 'nt' else 'clear')
    b = Board(28, 14)
    b.set_up()

    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    b.grid = array

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(b)
        b.new_generation()
        time.sleep(0.5)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    b = Board(70, 23)
    b.set_up()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(b)
        b.new_generation()
        time.sleep(0.25)


if __name__ == '__main__':
    main()
    #main_test()