def find_key(x, d):
    for (key, value) in d.items():
        if x in value:
            return key


forces = {}
curr_user = input()
users = []

while curr_user != "Lumpawaroo":

    if "|" in curr_user:
        side, user = curr_user.split(" | ")
        if side not in forces:
            forces[side] = []

        if user not in users:
            users.append(user)
            forces[side].append(user)

    elif "->" in curr_user:
        user, side = curr_user.split(" -> ")
        if side not in forces:
            forces[side] = []

        if user not in users:
            users.append(user)
            forces[side].append(user)
        else:
            curr_side = find_key(user, forces)
            forces[curr_side].remove(user)
            forces[side].append(user)
        print(f"{user} joins the {side} side!")

    curr_user = input()

for (side, users) in forces.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
    for u in users:
        print(f"! {u}")
