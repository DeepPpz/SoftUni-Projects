str_one, str_two = map(list, input().split())
result = 0

str_one = [ord(x) for x in str_one]
str_two = [ord(x) for x in str_two]

while True:
    if len(str_one) == 0:
        result += sum(str_two)
        break
    elif len(str_two) == 0:
        result += sum(str_one)
        break

    result += str_one[0] * str_two[0]
    str_one.pop(0)
    str_two.pop(0)

print(result)
