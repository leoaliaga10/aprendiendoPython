import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'db_python',
  'raise_on_warnings': True,
}

con = mysql.connector.connect(**config)

cursor = con.cursor()

cursor.execute("DELETE FROM ejemplo WHERE id='9'")

con.commit()

con.close()
