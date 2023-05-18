parentheses = list(input())
stacked_parentheses = []
balanced = True

for i in range(len(parentheses)):
    if parentheses[i] in ["{", "(", "["]:
        stacked_parentheses.append(parentheses[i])
    else:
        try:
            last_parentheses = stacked_parentheses.pop()

            if (parentheses[i] == '}' and not last_parentheses == "{") \
                    or (parentheses[i] == ')' and not last_parentheses == "(") \
                    or (parentheses[i] == ']' and not last_parentheses == "["):
                balanced = False
                break
        except IndexError:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
