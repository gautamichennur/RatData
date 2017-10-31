from flask import Flask, request, redirect
import os
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

# open a terminal window
# cd to ratchat directory
# ./ngrok http 5000
# copy webhook url
# open second terminal window
# cd to ratchat directory
# python receive_sms.py

app = Flask(__name__)
counter = 0

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    global counter
    
    response = MessagingResponse()
    message = Message()
    userInput = request.values.get("Body", None)

    print(userInput)

    if counter == 0:
         message.body("Hello! Please reply with one of the following numbers: \n 1. I saw a rat \n 2. I saw evidence of a rat"
        + "\n 3. I want to prevent rats \n 4. I have a question \n Type '1' or '2' or '3' or '4'")
    elif counter == 1:
        message.body("Where did you see the rat? \n 1. Inside \n 2.Outside \n Type '1' or '2'")
    elif counter == 2:
        message.body("Was the rat dead or alive? \n 1. Dead \n 2. Alive \n Type '1' or '2'")
    elif counter == 3:
        message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
    else:
        message.body("Outside valid case constraint")

    counter = counter + 1
    response.append(message)
    return str(response)



if __name__ == "__main__":
    app.run(debug=True)

    
