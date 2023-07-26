def read_next(*args, **kwargs):
    for el in args:
        for sym in el:
            yield sym
