def encrypt(letter):
    encryption = ""
    letter_code = ord(letter)
    
    encryption += chr(letter_code + letter_code % 10)
    encryption += str(letter_code)[0] + str(letter_code)[-1]
    encryption += chr(letter_code - int(str(letter_code)[0]))
    
    return encryption


count = int(input())
encrypted_string = ""

for _ in range(count):
    char = input()
    encrypted_string += encrypt(char)

print(encrypted_string)
