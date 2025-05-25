import pymysql
import sys

# add "users" table with exact columns mentioned below
class DBhelper:

    def __init__(self):
        try:

            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='madhu953',
                database='zomato'
            )

            self.mycursor = self.conn.cursor()
            print('Connected to Database')

        except:
            print('Some error occurred could not connect to database')
            sys.exit(0)

    def register(self, name, email, password):
        try:
            self.mycursor.execute('''
            INSERT INTO `users` (`user_id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            '''.format(name, email, password))
            self.conn.commit()
        except:
            return -1

        else:
            return 1

    def search(self, email, password):

        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email, password))

        data = self.mycursor.fetchall()
        return data
