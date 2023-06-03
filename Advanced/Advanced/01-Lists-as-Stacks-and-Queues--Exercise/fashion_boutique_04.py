stack = [int(x) for x in input().split()]
RACK_CAPACITY = int(input())
curr_rack = RACK_CAPACITY
racks = 1

while stack:
    curr_clothes = stack.pop()

    if curr_clothes < curr_rack:
        curr_rack -= curr_clothes
    elif curr_clothes == curr_rack:
        if stack:
            curr_rack = RACK_CAPACITY
            racks += 1
    else:
        curr_rack = RACK_CAPACITY - curr_clothes
        racks += 1

print(racks)
