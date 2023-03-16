import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    database = 'soft_uni'
)

mycursor = mydb.cursor()

sql = "INSERT INTO test_table (id) VALUES (4)"

mycursor.execute(sql)

mydb.commit()
mycursor.execute("SELECT * FROM test_table")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)