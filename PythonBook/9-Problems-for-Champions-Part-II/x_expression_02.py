expression = input()
symbols = list(expression)
result = 0
expression_operator = "+"

while True:
    symbol = symbols.pop(0)
    if symbol == "=":
        break

    if symbol == "(":
        inner_result = 0
        inner_operator = '+'
        
        while True:
            symbol = symbols.pop(0)
            
            if symbol == ")":
                if expression_operator == '+':
                    result += inner_result
                elif expression_operator == '-':
                    result -= inner_result
                elif expression_operator == '*':
                    result *= inner_result
                elif expression_operator == '/':
                    result /= inner_result
                break
            
            elif 0 <= ord(symbol) - ord('0') <= 9:
                if inner_operator == '+':
                    inner_result += ord(symbol) - ord('0')
                elif inner_operator == '-':
                    inner_result -= ord(symbol) - ord('0')
                elif inner_operator == '*':
                    inner_result *= ord(symbol) - ord('0')
                elif inner_operator == '/':
                    inner_result /= ord(symbol) - ord('0')
            
            elif symbol in ['+', '-', '*', '/']:
                inner_operator = symbol

    elif 0 <= ord(symbol) - ord('0') <= 9:
        if expression_operator == '+':
            result += ord(symbol) - ord('0')
        elif expression_operator == '-':
            result -= ord(symbol) - ord('0')
        elif expression_operator == '*':
            result *= ord(symbol) - ord('0')
        elif expression_operator == '/':
            result /= ord(symbol) - ord('0')
    
    elif symbol in ['+', '-', '*', '/']:
        expression_operator = symbol

print(f"{result:.2f}")
