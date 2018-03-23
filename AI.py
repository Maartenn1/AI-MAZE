import Look
import Move
import numpy as np

def Maarten1(maze, begin, eind):
    maze = maze
    path = [begin]
    lm = 4
    counter = 0
    moves = [Move.n, Move.e, Move.s, Move.w]
    while counter != 999:
        counter += 1
        moved = False
        self = path[-1]
        view = Look.look(maze, self)
        while not moved:
            if view[(lm - 2) % 8] != 0:
                path = moves[int(((lm / 2 + 1) - 2) % 4)](path)
                moved = True
                lm = (lm + 6) % 8
            else:
                lm = (lm + 2) % 8
        if path[-1] == eind:
            return path
    return path
