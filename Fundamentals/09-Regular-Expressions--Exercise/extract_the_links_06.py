import re

pattern = re.compile(r"www.([A-Za-z0-9-]+)(\.[a-z]+)+")

while True:
    data = input()
    if not data:
        exit()

    sites = re.finditer(pattern, data)

    for s in sites:
        print(s.group())
