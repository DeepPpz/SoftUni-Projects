from datetime import datetime
from datetime import timedelta

birth_date = input()

birth_date = datetime.strptime(birth_date, '%d-%m-%Y')
future_date = birth_date + timedelta(days=1000)

print('{:%d-%m-%Y}'.format(future_date))
