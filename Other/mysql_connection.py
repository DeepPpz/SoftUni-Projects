import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    database = 'sims_database'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT count(trait) FROM traits")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)