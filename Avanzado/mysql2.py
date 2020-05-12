import mysql.connector
#import sys

#print(sys.path)

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'db_python',
  'raise_on_warnings': True,
}

con = mysql.connector.connect(**config)

#con = mysql.connector.connect(user="root",password="root",host='127.0.0.1',database="db_python")

cursor = con.cursor()

#cursor.execute("CREATE TABLE ejemplo (id INT, data VARCHAR(100));")
#cursor.execute("INSERT INTO ejemplo (id,data) VALUES ('9','DATO')")
cursor.execute("SELECT * FROM ejemplo where id='9'")

rows = cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
con.close()
