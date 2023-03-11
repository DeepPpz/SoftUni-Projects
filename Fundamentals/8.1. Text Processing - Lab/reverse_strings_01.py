while True:
    word = input()

    if word == "end":
        exit(0)

    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")
