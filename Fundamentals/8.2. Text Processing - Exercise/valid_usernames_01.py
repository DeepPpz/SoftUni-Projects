from string import ascii_letters, digits

usernames = input().split(", ")
allowed_symbols = ascii_letters + digits + "-" + "_"

for user in usernames:
    if 3 <= len(user) <= 16:
        not_allowed = [x for x in user if x not in allowed_symbols]
        if not not_allowed:
            print(user)
