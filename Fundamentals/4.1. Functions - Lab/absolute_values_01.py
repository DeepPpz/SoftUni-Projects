values = input().split()

values = [abs(float(values[i])) for i in range(len(values))]

print(values)