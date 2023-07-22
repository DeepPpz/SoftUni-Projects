def get_max(in_type, a, b):
    result = None
    if in_type == "int":
        result = a if int(a) >= int(b) else b
    else:
        result = a if a >= b else b
    
    return result


input_type = input()
first_input = input()
second_input = input()

print(get_max(input_type, first_input, second_input))
