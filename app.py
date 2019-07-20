from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/sms", methods=['GET', 'POST'])
def sms():
  # Get the message the user sent our Twilio number
  body = request.values.get('Body', None)
  print(body)
  return body

if __name__ == "__main__":
  app.run()