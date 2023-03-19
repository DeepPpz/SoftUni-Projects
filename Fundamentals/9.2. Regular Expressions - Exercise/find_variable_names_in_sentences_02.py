import re

data = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, data)

for v in variables:
    v = v.replace("_", "")

print(*variables, sep=",")
