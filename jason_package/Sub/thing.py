
def min(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x if x < y else y
    else:
        raise Exception("Expected an int, but got x={}, y={}".format(type(x), type(y)))
