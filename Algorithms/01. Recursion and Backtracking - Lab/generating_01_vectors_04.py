def generate_vectors(idx):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        generate_vectors(idx + 1)


n = int(input())
vector = [0] * n

generate_vectors(0)
