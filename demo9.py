import sqlite3

conn = sqlite3.connect('test_demo_7.db')
cursor = conn.cursor()
cursor = cursor.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
cursor.close()
conn.commit()
conn.close()