import random
import sys


border_color = (0, 0, 0)
margin_color = (200, 200, 200)
background_color = (255, 255, 255)

def create_game_field(level):
    constructor = lambda: create_game_field(level - 1)
    if level == 1:
        constructor = lambda: '-'
    return [[constructor() for _ in range(3)] for _ in range(3)]


WIDTH = 1000
HEIGHT = 1000

white = (255, 255, 255)

LEVELS = 3
print(create_game_field(LEVELS))

min_cell_size = 20


class Cell:
    def __init__(self, level):
        self.level = level
        self.inner_cells = self.generate_inner_cells(level)

    def generate_inner_cells(self, level):
        # TODO
        return []


grid_width = min_cell_size
for level in range(1, LEVELS + 1):
    border = level
    margin = level
    grid_width = 3 * grid_width + border * 4 + margin * 2
    print(grid_width)


def draw_field(x, y, allocated_size, margin, border, level):
    if level == 0:
        return
    screen.draw.filled_rect(Rect((x, y), (allocated_size, allocated_size)), color=border_color)
    
    subcell_size = (allocated_size - border * 4 - 2 * margin) / 3

    for i in range(3):
        for j in range(3):
            
            sq_pos_x = x + border + margin + (subcell_size + border) * i
            sq_pos_y = y + border + margin + (subcell_size + border) * j

            screen.draw.filled_rect(
                Rect((sq_pos_x, sq_pos_y), (subcell_size, subcell_size)),
                color=margin_color    
            )
            draw_field(
                sq_pos_x + margin - 1,
                sq_pos_y + margin - 1,
                subcell_size - 2 * (margin - 1),
                border - 1,
                margin - 1,
                level - 1
            )


def draw():
    screen.fill(background_color)
    draw_field(WIDTH / 2 - grid_width / 2, HEIGHT / 2 - grid_width / 2, grid_width, LEVELS, LEVELS, LEVELS)
    pass


def update():
    pass
