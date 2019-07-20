import os
from twilio.rest import Client
from flask import Flask, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/', methods=['POST'])
def index():
	incomingMessageBody = request.values.get('Body', None)

	socketio.emit('message', incomingMessageBody)
	return incomingMessageBody

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)