n = int(input())

counter = 0
brackets = []
unbalanced = False

for i in range(n):
    line = input()

    if line not in ['(', ')']:
        continue
    elif line == '(' and counter == 0:
        brackets.append(line)
    elif line == ')' and counter == 0:
        unbalanced = True
        brackets.append(line)
    elif (line == '(' and brackets[counter - 1] != '(') or (line == ')' and brackets[counter - 1] == '('):
        brackets.append(line)
    else:
        unbalanced = True
        brackets.append(line)
    counter += 1

if unbalanced:
    print('UNBALANCED')
else:
    print('BALANCED')
