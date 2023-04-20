n = int(input())
f0, f1 = 1, 1

for i in range(n - 1):
    fn = f0 + f1
    f0 = f1
    f1 = fn

print(f1)
