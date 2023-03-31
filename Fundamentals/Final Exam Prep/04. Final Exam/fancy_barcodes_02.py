import re
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

n = int(input())

for _ in range(n):
    barcode = input()

    if re.match(pattern, barcode):
        group = ''.join([x for x in barcode if x.isdigit()])
        if not group:
            group = "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
