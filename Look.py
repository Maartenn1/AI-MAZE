import numpy as np
def look(maze, self):
    selfx= self[1]
    selfy= self[0]
    me = maze[self[0]][self[1]]
    n = kijk(maze, -1, 0, selfy, selfx)
    ne = kijk(maze, -1, 1, selfy, selfx)
    e = kijk(maze, 0, 1, selfy, selfx)
    se = kijk(maze, 1, 1, selfy, selfx)
    s = kijk(maze, 1, 0, selfy, selfx)
    sw = kijk(maze, 1, -1, selfy, selfx)
    w = kijk(maze, 0, -1, selfy, selfx)
    nw = kijk(maze, -1, -1, selfy, selfx)
    view = np.array([n, ne, e, se, s, sw, w, nw])
    return view


def kijk(maze, y, x, selfy, selfx):
    if selfy + y >= 0 and selfx + x >= 0:
        try:
            r = maze[selfy + y][selfx + x]
        except IndexError:
            r = 0
    else:
        r = 0
    return r
