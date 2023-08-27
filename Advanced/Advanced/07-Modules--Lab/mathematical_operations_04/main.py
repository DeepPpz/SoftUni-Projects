from package.perform_calculations import *


while True:
    input_string = input()
    
    if input_string == "":
        break
    
    print(perform_calculation(input_string))
