string_line = input().split()
check_palindrome = input()

palindromes = [el for el in string_line if el == el[::-1]]
occurrences = palindromes.count(check_palindrome)

print(palindromes)
print(f'Found palindrome {occurrences} times')