class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    info = input().split()

    if info[0] == 'Stop':
        break

    sender = info[0]
    receiver = info[1]
    content = info[2]

    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(', ')))

for i in send_emails:
    emails[i].send()

for e in emails:
    print(e.get_info())