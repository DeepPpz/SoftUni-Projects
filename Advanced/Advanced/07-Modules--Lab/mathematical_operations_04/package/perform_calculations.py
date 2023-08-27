def perform_calculation(string):
    num_one, sign, num_two = string.split()
    num_one, num_two = float(num_one), float(num_two)

    if sign == "/":
        result = num_one / num_two
    elif sign == "*":
        result = num_one * num_two
    elif sign == "-":
        result = num_one - num_two
    elif sign == "+":
        result = num_one + num_two
    elif sign == "^":
        result = num_one ** num_two
    else:
        return "Invalid operation"

    formatted_result = "{:.2f}".format(result)
    return formatted_result
