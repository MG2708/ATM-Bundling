import mysql.connector
mydb=mysql.connector.connect(host='156.67.222.190',user='u518149110_admin',password='Ke460qIg~4t')
mycursor=mydb.cursor()
mycursor.execute("Use u518149110_atm")
mycursor.execute("Drop Table users")
for x in mycursor:
    print(x)
