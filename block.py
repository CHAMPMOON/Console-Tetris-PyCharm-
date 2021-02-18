import msvcrt

class Block:
    def __init__(self, number, width):
        if number == 1:
            self.block = [[0, width // 2], [0, width // 2 + 1], [0, width // 2 + 2], [0, width // 2 + 3]]
        if number == 2:
            self.block = [[1, width // 2 + 1], [0, width // 2 + 1], [0, width // 2 + 2], [1, width // 2 + 2]]
        if number == 3:
            self.block = [[0, width // 2 + 1], [0, width // 2 + 2], [1, width // 2 + 2], [1, width // 2 + 3]]
        if number == 4:
            self.block = [[1, width // 2 + 1], [0, width // 2 + 2], [1, width // 2 + 2], [0, width // 2 + 3]]
        if number == 5:
            self.block = [[1, width // 2 + 1], [1, width // 2 + 2], [1, width // 2 + 3], [0, width // 2 + 2]]
        if number == 6:
            self.block = [[1, width // 2 + 1], [1, width // 2 + 2], [1, width // 2 + 3], [0, width // 2 + 3]]
        if number == 7:
            self.block = [[1, width // 2 + 1], [1, width // 2 + 2], [1, width // 2 + 3], [0, width // 2 + 1]]

    def fall_block(self, arena):
        for index in self.block:
            if arena.arena[index[0] + 1][index[1]] != '  ':
                return "border"
        for index in self.block:
            index[0] += 1

    def check_start(self, arena):
        for index in self.block:
            if arena.arena[index[0]][index[1]] != '  ':
                return "game over"

    def position_block_right(self, arena):
        for index in self.block:
            if arena[index[0]][index[1] + 1] != '  ':
                return 0

    def position_block_left(self, arena):
        for index in self.block:
            if arena[index[0]][index[1] - 1] != '  ':
                return 0

    def position_block_down(self, arena):
        for index in self.block:
            if arena[index[0] + 1][index[1]] != '  ':
                return 0


    def move_block(self, arena):
        if msvcrt.kbhit():
            pressedKey = msvcrt.getch()
            if ord(pressedKey) == 77:
                if self.position_block_right(arena.arena) == 0: return
                for index in self.block:
                    index[1] += 1
            if ord(pressedKey) == 75:
                if self.position_block_left(arena.arena) == 0: return
                for index in self.block:

                    index[1] -= 1
            if ord(pressedKey) == 80:
                if self.position_block_down(arena.arena) == 0: return
                for index in self.block:
                    index[0] += 1
            if ord(pressedKey) == 72:
                self.turn_block(arena)

    def turn_block(self, arena):
        min_x = min(self.block, key=lambda x: x[0])[0]
        max_x = max(self.block, key=lambda x: x[0])[0]

        min_y = min(self.block, key=lambda x: x[1])[1]
        max_y = max(self.block, key=lambda x: x[1])[1]

        new_block = []
        if (max_y - min_y) > (max_x - min_x):
            count = 0
            if min_x != max_x:
                for i in range(min_y, max_y + 1):
                    if [min_x, i] in self.block:
                        new_block.append([min_x + count, max_y])
                    if [max_x, i] in self.block:
                        new_block.append([min_x + count, max_y - 1])
                    count += 1
            else:
                for i in range(min_y, max_y + 1):
                    new_block.append([min_x + count, max_y])
                    count += 1
        else:
            count = 0
            if max_y != min_y:
                for i in range(min_x, max_x + 1):
                    if [i, min_y] in self.block:
                        new_block.append([max_x - 1, max_y - count])
                    if [i, max_y] in self.block:
                        new_block.append([max_x, max_y - count])
                    count += 1
            else:
                for i in range(min_x, max_x + 1):
                    new_block.append([max_x, max_y - count])
                    count += 1

        if self.check_block(arena, new_block) == 0:
            return
        else:
            self.block = new_block

    def check_block(self, arena, new_block):
        for x, y in new_block:
            if arena.arena[x][y] != '  ':
                if [x, y] not in self.block:
                    return 0

