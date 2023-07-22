def genrange(start, end):
    num = start
    
    while num <= end:
        yield num
        num += 1
