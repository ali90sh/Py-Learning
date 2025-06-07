import mysql.connector

config = {
  'user': 'report_user',
  'password': 'StrongPass123!',
  'host': '127.0.0.1',
  'database': 'employee',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT * FROM employees ")
cursor.execute(query)
# print(type(cursor))
sorted_cursor = sorted(cursor, key = lambda x: (-x[2], x[1]))

for name, weight, height in sorted_cursor:
    print(f'{name} {height} {weight}')
    
cursor.close()
cnx.close()