import random

def create_game_field(level):
    constructor = lambda: create_game_field(level - 1)
    if level == 1:
        constructor = lambda: '-'
    return [[constructor() for _ in range(3)] for _ in range(3)]


WIDTH = 500
HEIGHT = 500

white = (255, 255, 255)

LEVELS = 2
print(create_game_field(LEVELS))

min_cell_size = 20

grid_width = min_cell_size
for level in range(1, LEVELS + 1):
    border = level
    margin = level
    grid_width = 3 * grid_width + border * 4 + margin * 2
    print(grid_width)


def draw():
    #TODO recursively draw field
    pass


def update():
    pass
