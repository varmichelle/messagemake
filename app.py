import os
from twilio.rest import Client
from flask_socketio import SocketIO
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
socketio = SocketIO(app)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/sms", methods=['GET', 'POST'])
def sms():
  if request.method == 'POST':
    # Get the message the user sent our Twilio number
    incomingMessageBody = request.values.get('Body', None)

    # Reply with the same message
    message = client.messages \
    .create(
        body=incomingMessageBody,
        from_='+12055572027',
        to='+19784831084'
    )
    print(message.sid)
    return incomingMessageBody
  
  if request.method == 'GET':
    return "sms page"

if __name__ == "__main__":
  socketio.run(app)