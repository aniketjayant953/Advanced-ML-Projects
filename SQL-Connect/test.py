import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='madhu953',
    database='zomato'
)

cursor = conn.cursor()
print('Connected to Database')
