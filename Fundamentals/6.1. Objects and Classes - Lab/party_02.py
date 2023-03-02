class Party:
    def __init__(self):
        self.people = []


party = Party()
names = input()

while names != 'End':
    party.people.append(names)
    names = input()

print('Going: ' + ', '.join(party.people))
print('Total: ' + str(len(party.people)))