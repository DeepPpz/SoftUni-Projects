def reverse_text(string):
    i = len(string)
    
    while i > 0:
        i -= 1
        yield string[i]


for char in reverse_text("step"):
    print(char, end='')
