import re

data = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = re.findall(pattern, data)

print(*names, sep=' ')
