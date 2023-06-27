key = int(input())
n = int(input())

message = ''

for i in range(n):
    letter = ord(input())
    letter += key
    message += chr(letter)

print(message)
