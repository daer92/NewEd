

def percents(x, y):
    """what percents x of y"""
    one_percent = x // 100
    result = y // one_percent
    return result

def print_percent(x, y):
    print(str(y) + " is " + str(percents(x, y)) + " persents of " + str(x))

print_percent(100, 50)
