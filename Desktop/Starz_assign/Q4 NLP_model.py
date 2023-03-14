import openai
import twilio
from twilio.twiml.messaging_response import MessagingResponse


openai.api_key = "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"


account_sid = "YOUR_ACCOUNT_SID_HERE"
auth_token = "YOUR_AUTH_TOKEN_HERE"
client = twilio.rest.Client(account_sid, auth_token)


def handle_message(message_body):
  
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message_body,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
    )
   
    response_text = response.choices[0].text.strip()

   
    twiml_response = MessagingResponse()
    
    twiml_response.message(response_text)

   
    return str(twiml_response)

# Set up the Flask app to handle incoming messages
from flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def handle_sms():
    message_body = request.form["Body"]
    twiml_response = handle_message(message_body)
    return twiml_response, 200, {"Content-Type": "application/xml"}

if __name__ == "__main__":
    app.run(debug=True)
