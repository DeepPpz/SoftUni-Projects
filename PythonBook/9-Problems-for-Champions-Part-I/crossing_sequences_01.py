first_num = int(input())
second_num = int(input())
third_num = int(input())
spiral_curr = int(input())
spiral_step = int(input())

tribonacci_numbers = [first_num, second_num, third_num]
curr_num = third_num

while curr_num < 1000000:
    curr_num = first_num + second_num + third_num
    tribonacci_numbers.append(curr_num)

    first_num = second_num
    second_num = third_num
    third_num = curr_num

spiral_numbers = [spiral_curr]
counter = 0
step_mul = 1

while spiral_curr < 1000000:
    spiral_curr += spiral_step * step_mul
    spiral_numbers.append(spiral_curr)
    counter += 1

    if counter % 2 == 0:
        step_mul += 1

found = False
for i in range(len(tribonacci_numbers)):
    for j in range(len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j] and tribonacci_numbers[i] <= 1000000:
            found = True
            print(tribonacci_numbers[i])
    if found:
        break

if not found:
    print('No')
