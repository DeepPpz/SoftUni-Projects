from package.fibonacci_sequence import *


fibonacci = FibonacciSequence()

while True:
    command = input().split()
    
    if command[0] == "Stop":
        break
    elif command[0] == "Create":
        count = int(command[2])
        sequence = fibonacci.create_sequence(count)
        print(" ".join(map(str, sequence)))
    elif command[0] == "Locate":
        number = int(command[1])
        result = fibonacci.locate_number(number)
        print(result)
