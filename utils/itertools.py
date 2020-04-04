def count(start: int = 0, step: int = 1):
    n = start
    while True:
        yield n
        n += step
