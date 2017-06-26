from functools import reduce


def pipe(functions_to_pipe):
    def wrapped(*args):
        origin = None if len(args) == 0 else args[0]
        return reduce((lambda x, y: y(x)), functions_to_pipe, origin)
    return wrapped
