# This will run an api on local host where you can chat with sql
from flask import Flask, jasonify
from chatSQL import ChatWithSQL

app = Flask(__name__)
obj = ChatWithSQL('root','madhu953', 'localhost','zomato')
@app.route('/send-message', methods=['GET'])
def send_message():
    # message = "Hello, This is a message from the Flask API"
    message = obj.message('How many rows do we have in this database?')
    return jasonify({'message':message})

if __name__ == "__main__":
    app.run(debug=True)
    