number = int(input())

prime_flag = True

for i in range(2, number):
    if number % i == 0:
        prime_flag = False
        break

if prime_flag:
    print('True')
else:
    print('False')