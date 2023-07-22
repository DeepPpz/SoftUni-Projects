guess_number = input()
target_bulls = int(input())
target_cows = int(input())
solution_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                guess_a = int(guess_number[0:1])
                guess_b = int(guess_number[1:2])
                guess_c = int(guess_number[2:3])
                guess_d = int(guess_number[3:4])

                digit_a_check = a
                digit_b_check = b
                digit_c_check = c
                digit_d_check = d

                current_bulls = 0
                current_cows = 0

                if digit_a_check == guess_a:
                    current_bulls += 1
                    guess_a = -1
                    digit_a_check = -2
                
                if digit_b_check == guess_b:
                    current_bulls += 1
                    guess_b = -1
                    digit_b_check = -2
                
                if digit_c_check == guess_c:
                    current_bulls += 1
                    guess_c = -1
                    digit_c_check = -2
                
                if digit_d_check == guess_d:
                    current_bulls += 1
                    guess_d = -1
                    digit_d_check = -2

                if digit_a_check == guess_b:
                    current_cows += 1
                    guess_b = -1
                elif digit_a_check == guess_c:
                    current_cows += 1
                    guess_c = -1
                elif digit_a_check == guess_d:
                    current_cows += 1
                    guess_d = -1

                if digit_b_check == guess_a:
                    current_cows += 1
                    guess_a = -1
                elif digit_b_check == guess_c:
                    current_cows += 1
                    guess_c = -1
                elif digit_b_check == guess_d:
                    current_cows += 1
                    guess_d = -1

                if digit_c_check == guess_a:
                    current_cows += 1
                    guess_a = -1
                elif digit_c_check == guess_b:
                    current_cows += 1
                    guess_b = -1
                elif digit_c_check == guess_d:
                    current_cows += 1
                    guess_d = -1

                if digit_d_check == guess_a:
                    current_cows += 1
                    guess_a = -1
                elif digit_d_check == guess_b:
                    current_cows += 1
                    guess_b = -1
                elif digit_d_check == guess_c:
                    current_cows += 1
                    guess_c = -1

                if current_bulls == target_bulls and current_cows == target_cows:
                    if solution_found:
                        print(" ", end="")
                    print(f"{a}{b}{c}{d}", end="")
                    solution_found = True

if not solution_found:
    print("No")
