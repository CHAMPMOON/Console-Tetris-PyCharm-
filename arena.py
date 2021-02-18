import os
import copy
import time

class Arena:
    def __init__(self, length, width):
        self.arena = [""] * length
        for i in range(0, len(self.arena) - 1):
            self.arena[i] = ['#', '#'] + ['  '] * width + ['#', '#']
        self.arena[-1] = ['#'] * (width + 2) * 2

    @staticmethod
    def print(arena):
        shift = '\t' * 6
        work = "\n"
        for i in arena:
            work += shift + "".join(i) + "\n"
        print(work)

    def shave_line(self, lenght, width):
        bound = 0
        for i in range(lenght - 2, 0, -1):
            count = self.arena[i].count('☐ ')
            if count == width:
                if count % 2 == 0:
                    for j in range(1, width // 2 + 1):
                        self.arena[i][j + width // 2 + 1] = '  '
                        self.arena[i][width // 2 + 2 - j] = '  '
                        self.update(0.1)
                        Arena.print(self.arena)
                    bound = i
                else:
                    self.arena[i][width // 2 + 2] = '  '
                    self.update(0.1)
                    Arena.print(self.arena)
                    for j in range(1, width // 2 + 1):
                        self.arena[i][j + width // 2 + 2] = '  '
                        self.arena[i][width // 2 + 2 - j] = '  '
                        self.update(0.1)
                        Arena.print(self.arena)
                    bound = i
        if bound != 0:
            for i in range(bound, 0, -1):
                self.arena[i] = copy.deepcopy(self.arena[i - 1])

    def show_block(self, block):
        test = copy.deepcopy(self.arena)
        for ind in block.block:
            test[ind[0]][ind[1]] = '☐ '
        Arena.print(test)

    def add_block(self, block):
        for ind in block.block:
            self.arena[ind[0]][ind[1]] = '☐ '

    def game_over(self):
        os.system("cls")
        Arena.print(self.arena)
        print('\t' * 7, "GAME OVER")

    def update(self, period):
        time.sleep(period)
        os.system("cls")













