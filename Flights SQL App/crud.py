import mysql.connector

# connect to the database
try:
    conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='madhu953',
                                   database='zomato')

    cursor = conn.cursor()
    print('Connection Established')

except:
    print('Connection error')

# create a table
# airport -> airport | code | name

# cursor.execute('''
# CREATE TABLE airport (
#         airport_id INT PRIMARY KEY,
#         code  VARCHAR(10) NOT NULL,
#         city VARCHAR(50) NOT NULL,
#         name VARCHAR(50) NOT NULL
#         )
# ''')

# conn.commit()

#  Insert data to table
# cursor.execute("""
# INSERT INTO airport values
# (1, 'DEL','New Delhi','IGIA'),
# (2, 'CCU','Kolkata','NSCA'),
# (3, 'BOM','Mumbai','CSMA')
# """)
# conn.commit()

# Search/Retrieve

cursor.execute('SELECT * FROM airport WHERE airport_id > 1')
data = cursor.fetchall()
print(data)

for i in data:
    print(i[3])

# Update
cursor.execute("""
UPDATE airport
SET city = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

cursor.execute('SELECT * FROM airport')
data = cursor.fetchall()
print(data)

# Delete
cursor.execute("""
DELETE FROM airport
WHERE city = 'Bombay'
""")
conn.commit()

cursor.execute('SELECT * FROM airport')
data = cursor.fetchall()
print(data)