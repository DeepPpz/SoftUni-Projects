import re
pattern = re.compile(r"(?P<cust>%[A-Z][a-z]+%)([^|$%.])*(?P<prod><\w+>)([^|$%.])*"
                     r"(?P<count>\|\d+\|)([^|$%.])*(?P<price>[1-9][.0-9]*\$)")
total_income = 0

while True:
    order = input()

    if order == "end of shift":
        print(f"Total income: {total_income:.2f}")
        exit(0)

    valid_order = re.match(pattern, order)

    if valid_order:
        customer = valid_order.group("cust").strip("%")
        product = valid_order.group("prod").lstrip("<").rstrip(">")
        total_price = float(valid_order.group("count").strip("|")) * float(valid_order.group("price").rstrip("$"))

        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")
