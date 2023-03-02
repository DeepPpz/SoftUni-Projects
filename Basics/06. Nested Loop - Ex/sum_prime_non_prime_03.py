number = input()

sum_prime = 0
sum_nonprime = 0

while number != 'stop':
    number = int(number)

    if number < 0:
        print('Number is negative.')
        number = input()
        continue

    for i in range(2, number):
        if number % i == 0:  # non-prime
            sum_nonprime += number
            break
    else:  # prime
        sum_prime += number

    number = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_nonprime}')