text = input().split()

cleared_text = [el for el in text if len(el) % 2 == 0]

print(*cleared_text, sep='\n')
