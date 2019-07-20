from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/sms", methods=['GET', 'POST'])
def sms():
  # Get the message the user sent our Twilio number
  body = request.values.get('Body', None)
  print(body)
  return body

if __name__ == "__main__":
  app.run()