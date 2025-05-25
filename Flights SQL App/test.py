import mysql.connector
class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='madhu953',
                database='zomato'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection error')

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights
        UNION
        SELECT DISTINCT(Source) FROM flights
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_flights(self, source, destination):

        self.mycursor.execute(f"""
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights
        WHERE Source = '{source}' AND Destination = '{destination}'
        """)

        data = self.mycursor.fetchall()

        return data

    def fetch_freq(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM flights
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT 
        Source, COUNT(*)
        FROM
            (SELECT 
                source
            FROM
                flights UNION ALL SELECT 
                destination
            FROM
                flights) T
        GROUP BY T.Source
        ORDER BY count(*) desc
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_freq(self):
        date = []
        frequency = []

        self.mycursor.execute("""
        select Date_of_Journey, COUNT(*) FROM flights
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency


import mysql.connector
print("Module loaded successfully")