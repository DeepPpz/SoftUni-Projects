paper_amount = int(input())
cloth_amount = int(input())
glue_amount = float(input())
discount = int(input())

discount /= 100

paper_sum = paper_amount * 5.80 * (1 - discount)
cloth_sum = cloth_amount * 7.20 * (1 - discount)
glue_sum = glue_amount * 1.20 * (1 - discount)

total_sum = paper_sum + cloth_sum + glue_sum

print(f'{total_sum:.3f}')
