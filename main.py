from arena import Arena
from block import Block
import random
length = 15
width = 10


arena = Arena(length, width)
block = Block(random.randint(1, 7), width)

period = 0
while True:
    period += 1
    block.move_block(arena)
    arena.show_block(block)
    if period == 5:
        period = 0
        if block.fall_block(arena) == "border":
            arena.add_block(block)
            arena.shave_line(length, width)
            block = Block(random.randint(1, 7), width)
            if block.check_start(arena) == "game over":
                arena.game_over()
                break
    arena.update(0.05)


