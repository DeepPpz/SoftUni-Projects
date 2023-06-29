algebraic_expression = input()
indexes = []

for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == "(":
        indexes.append(i)
    if algebraic_expression[i] == ")":
        start_str = indexes.pop()
        end_str = i + 1
        print(algebraic_expression[start_str:end_str])
