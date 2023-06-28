# player: {position: skill}

def dueling_players(player1, player2):
    if player1 in statistics and player2 in statistics:
        skill1 = sum(x for x in statistics[player1]. values())
        skill2 = sum(x for x in statistics[player2].values())
    else:
        return

    for pos1 in statistics[player1]:
        for pos2 in statistics[player2]:
            if pos1 == pos2:
                if skill1 > skill2:
                    del statistics[player2]
                elif skill2 > skill1:
                    del statistics[player1]
                return


def adding_players(player, position, skill):
    if player not in statistics:
        statistics[player] = {position: skill}
    elif position not in statistics[player]:
        statistics[player][position] = skill
    else:
        curr_skill = statistics[player][position]
        statistics[player][position] = max(curr_skill, skill)


statistics = {}

while True:
    command = input()

    if command == "Season end":
        break
    elif " vs " in command:
        command = command.split(" vs ")
        dueling_players(command[0], command[1])
    else:
        command = command.split(" -> ")
        adding_players(command[0], command[1], int(command[2]))

statistics = dict(sorted(statistics.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for player in statistics:
    print(f"{player}: {sum(statistics[player].values())} skill")
    for (position, skill) in sorted(statistics[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
