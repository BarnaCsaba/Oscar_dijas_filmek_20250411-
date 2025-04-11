import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='oscar')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM film")

for x in mycursor:
    print(x)

#2-es feladat
mycursor.execute("""SELECT ev, cim FROM film
WHERE nyert = 1
ORDER BY ev ASC;""")

for x in mycursor:
    print(x)
