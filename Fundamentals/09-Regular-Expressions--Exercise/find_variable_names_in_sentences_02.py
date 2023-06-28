import re

data = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, data)

for i in range(len(variables)):
    variables[i] = variables[i].replace("_", "")

print(*variables, sep=",")
