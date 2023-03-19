import re

data = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = re.finditer(pattern, data)

for n in numbers:
    print(n.group(), end=" ")
