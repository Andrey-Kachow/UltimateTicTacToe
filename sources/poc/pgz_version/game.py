import random

def create_game_field(level):
    constructor = lambda: create_game_field(level - 1)
    if level == 0:
        constructor = lambda: '-'
    return [[constructor() for _ in range(3)] for _ in range(3)]


WIDTH = 500
HEIGHT = 500

white = (255, 255, 255)

levels = 2
print(create_game_field(levels))

def draw():
    pass


def update():
    pass
