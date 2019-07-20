import os
from twilio.rest import Client
from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return "hello world!"
	if request.method == 'POST':
		incomingMessageBody = request.values.get('Body', None)
		socketio.emit('message', incomingMessageBody)
		return incomingMessageBody

if __name__ == '__main__':
	socketio.run(app)