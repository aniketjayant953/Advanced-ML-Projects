import sys
from dbhelper import DBhelper


class Flipkart:

    def __init__(self):
        # connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input = input('''
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        ''')

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(1000)

    def login_menu(self):
        user_input = input('''
                1. Enter 1 to see profile
                2. Enter 2 to edit profile
                3. Enter 3 to delete profile
                4. Enter 4 to logout
                ''')

    def register(self):
        name = input('Enter the name: ')
        email = input('Enter email: ')
        password = input('Enter the password: ')

        response = self.db.register(name, email, password)

        if response:
            print('Registration successful')
        else:
            print("Registration failed")

        self.menu()

    def login(self):
        email = input('Enter email: ')
        password = input('Enter the password: ')

        data = self.db.search(email, password)

        if len(data) == 0:
            print('Incorrect email/password')
        else:
            print('Hello', data[0][1])

        self.login_menu()


obj = Flipkart()
