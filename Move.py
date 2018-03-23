def s(path):
    path.append([path[-1][0] + 1, path[-1][1]])
    return path


def n(path):
    path.append([path[-1][0] - 1, path[-1][1]])
    return path

def e(path):
    path.append([path[-1][0], path[-1][1] + 1])
    return path

def w(path):
    path.append([path[-1][0], path[-1][1] - 1])
    return path