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
currCase = 0
dict_alive = {"1": "Dead", "2": "Alive"}
dict_location = {"1": "Inside", "2": "Outside"}
dict_evidence = {"1": "Rat Droppings", "2":"Chewed boxes or food"}

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    global counter
    global currCase
    global dict_alive
    global dict_evidence
    global dict_location


    response = MessagingResponse()
    message = Message()
    userInput = request.values.get("Body", None)

    print(userInput)

    if (counter == 0):
        message.body("Hello! Please reply with one of the following numbers: \n 1. I saw a rat \n 2. I saw evidence of a rat"
        + "\n 3. I want to prevent rats \n Type '1' or '2' or '3'")
        counter = counter + 1
        response.append(message)
        return str(response)
        #print (counter)
        #print (userInput)
        #print (currCase)

    if (currCase == 1 and counter == 4):
        message.body("Thank you for your response!")
        print(dict_alive[userInput])
        currCase = 0
        counter = 0
        userInput = 0

    if (currCase == 1 and (userInput == "1" or userInput == "2") and counter == 3):
        message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
        counter = counter + 1
        #print (userInput)
        #print (currCase)
        #print (counter)
    elif (currCase == 2 and counter == 3):
        message.body("Thank you for your response!")
        currCase = 0
        counter = 0
        userInput = 0
    elif (counter == 3):
        message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
        userInput = 0
        counter = 0
        currCase = 0

    if (currCase == 1 and counter == 2 and (userInput == "1" or userInput == "2")):
        message.body("Was the rat dead or alive? \n 1. Dead \n 2. Alive \n Type '1' or '2'")
        counter = counter + 1
        print (dict_location[userInput])
        #print (userInput)
        #print (counter)
        #print (currCase)
    elif (currCase == 2 and (userInput == "1" or userInput == "2") and counter == 2):
        message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
        counter = counter + 1
        print (dict_evidence[userInput])
        #print (counter)
        #print (currCase)
    elif (counter == 2):
        message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
        userInput = 0
        counter = 0
        currCase = 0


    if (userInput == "1" and counter == 1):
        message.body("Where did you see the rat? \n 1. Inside \n 2.Outside \n Type '1' or '2'")
        counter = counter + 1
        currCase = 1

        #print (userInput)
        #print (counter)
        #print (currCase)
    elif (userInput == "2" and counter == 1):
        message.body("Please categorize your evidence:\n 1.Rat Droppings\n 2.Chewed boxes or food \n Type '1' or '2'")
        counter = counter + 1
        currCase = 2

        #print (userInput)
        #print (counter)
        #print (currCase)
    elif (userInput == "3" and counter == 1):
        message.body("Thank you for your interest in rat prevention. Please follow this link for more info: linkhere")
        counter = 0
        currCase = 0
        #print (userInput)
        #print (counter)
        #print (currCase)
    elif(counter == 1):
        message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
        userInput = 0
        counter = 0
        currCase = 0



    response.append(message)
    return str(response)



if __name__ == "__main__":
    app.run(debug=True)
