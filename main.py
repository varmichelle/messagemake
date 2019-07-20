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

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		incomingMessageBody = request.values.get('Body', None)

		# Reply with the same message
		message = client.messages \
		.create(
			body=incomingMessageBody,
			from_='+12055572027',
			to='+19784831084'
		)
		print(message.sid)

		socketio.emit('message', incomingMessageBody)
		return incomingMessageBody
	else:
		return "message sent"

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)