import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='oscar')
mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM film")
#
#for x in mycursor:
#    print(x)

#2-es feladat
mycursor.execute("""SELECT ev, cim FROM film
WHERE nyert = 1
ORDER BY ev ASC
LIMIT 20""")

for x in mycursor:
    print(x)

#3.feladat
mycursor.execute("""SELECT ev FROM film
GROUP BY ev
HAVING COUNT(ev) >= 10;""")

for x in mycursor:
    print(x)

##4.feladat
#cursor.execute("""SELECT * FROM film
#WHERE ev >= 1939 AND ev <= 1945;""")
#
#for x in cursor:
#    print(x)

#5.feladat

#cursor.execute("""SELECT cim FROM film
#WHERE nyert = 1 AND bemutato > ;""")

#for x in cursor:
 #   print(x)

 #6.feladat