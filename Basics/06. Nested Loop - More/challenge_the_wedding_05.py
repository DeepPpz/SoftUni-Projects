male_count = int(input())
female_count = int(input())
max_tables = int(input())

table_counter = 1

for m in range(1, male_count + 1):
    for f in range(1, female_count + 1):
        if table_counter <= max_tables:
            print(f'({m} <-> {f})', end= ' ')
            table_counter += 1