from flask import Flask, request, redirect
import os
import xlsxwriter
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
# workbook = xlsxwriter.Workbook('test_data.xlsx')
# worksheet = workbook.add_worksheet()
# row_counter = 1

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    global counter
    global case
    global dict_alive
    global dict_evidence
    global dict_location



    response = MessagingResponse()
    message = Message()
    userInput = request.values.get("Body", None)

    #prints what Twilio user texts the bot. Runs each time the user texts.
    print(userInput)

    # ---------- CASE 0: BASE CASE ---------------------------
    # ---------- counter: 0 ---------------
    # ---------- case: 0 -----------------
    if (counter == 0):
        message.body("Hello! Please reply with one of the following numbers:"
        + "\n 1. I saw a rat \n 2. I saw evidence of a rat"
        + "\n 3. I want to prevent rats \n Type '1' or '2' or '3'")
        counter = counter + 1
        response.append(message)
        return str(response)

        #print (counter)
        #print (userInput)
        #print (currCase)
    #------------------- SET CASES --------------------------------
    if (userInput == "1" and counter == 1):
        case = 1
    elif (userInput == "2" and counter == 1):
        case = 2
    elif (userInput == "3" and counter == 1):
        case = 3
    else:
        message.body("Sorry looks like there was an error."
        + " Please enter only the numbers provided as an option."
        + "\n Type 'RAT' to return to the main menu!")
        #reset counters, back to case 0
        counter = 0
        case = 0


    #-------------------- CASE LOGIC -----------------------------
    if (case == 1):
        if (counter == 1):
            message.body("Where did you see the rat? \n 1. Inside \n 2.Outside \n Type '1' or '2'")
            counter = counter + 1

        elif (counter == 2 and (userInput == "1" or userInput == "2")):
            message.body("Was the rat dead or alive? \n 1. Dead \n 2. Alive \n Type '1' or '2'")
            counter = counter + 1

            #response for rat sighting: "was the rat inside or outside?"
            print (dict_location[userInput])

        elif (counter == 3 and (userInput == "1" or userInput == "2")):
            message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
            counter = counter + 1

            #resonse for rat sighting: "was the rat dead or alive?"
            print (dict_alive[userInput])

        elif (counter == 4):
            message.body("Thank you for your response!")
            #resetting the counters, back to case 0
            case = 0
            counter = 0

        else:
            #---------ERROR--------------
            message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option."
            + "\n Type 'RAT' to return to the main menu!")
            #reset counters, back to case 0
            counter = 0
            case = 0

    elif (case == 2):
        if (counter == 1):
            message.body("Please categorize your evidence:\n 1.Rat Droppings\n 2.Chewed boxes or food \n Type '1' or '2'")
            counter = counter + 1

        elif (counter == 2 and (userInput == "1" or userInput == "2")):
            message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
            counter = counter + 1

            #response for rat evidence: "what type of evidence?"
            print (dict_evidence[userInput])

        elif (counter == 3):
            message.body("Thank you for your response!")
            #resetting counters, back to case 0
            case = 0
            counter = 0


        else:
            #-----------ERROR------------
            message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option."
            + "\n Type 'RAT' to return to the main menu!")
            #reset counters, back to case 0
            counter = 0
            case = 0

    elif (case == 3):
        if (counter == 1):
            message.body("Thank you for your interest in rat prevention. Please follow this link for more info: linkhere")
            counter = 0
            case = 0


    # OLD CODE
    # # ------------ CASE 1, Thank you response --------------------------
    # if (currCase == 1 and counter == 4):
    #     message.body("Thank you for your response!")
    #
    #     #resetting the counters, back to case 0
    #     currCase = 0
    #     counter = 0
    #     userInput = 0
    #
    #
    # # ----------- CASE 1, rat sighting: Location/Address ---------------------
    # if (currCase == 1 and (userInput == "1" or userInput == "2") and counter == 3):
    #     message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
    #     counter = counter + 1
    #
    #     #resonse for rat sighting: "was the rat inside or outside?"
    #     print (dict_alive[userInput])
    #
    #
    #     #print (userInput)
    #     #print (currCase)
    #     #print (counter)
    #
    # # ---------- CASE 2, Thank you response --------------------------------
    # elif (currCase == 2 and counter == 3):
    #     message.body("Thank you for your response!")
    #
    #     #resetting counters, back to case 0
    #     currCase = 0
    #     counter = 0
    #     userInput = 0
    #
    # # ------------ CASE 3, ERROR --------------------------------------------
    # elif (counter == 3):
    #     message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
    #
    #     #TODO change error type to go back one step not back to beginning
    #     #resets counters to case 0
    #     userInput = 0
    #     counter = 0
    #     currCase = 0
    #
    # # ------------- CASE 1, rat sighting: dead/alive ----------------------
    # if (currCase == 1 and counter == 2 and (userInput == "1" or userInput == "2")):
    #     message.body("Was the rat dead or alive? \n 1. Dead \n 2. Alive \n Type '1' or '2'")
    #     counter = counter + 1
    #
    #     #response for rat sighting: "was the rat inside or outside?"
    #     print (dict_location[userInput])
    #
    #     #print (userInput)
    #     #print (counter)
    #     #print (currCase)
    #
    # # ------------ CASE 2, rat evidence: location/address ----------------------
    # elif (currCase == 2 and (userInput == "1" or userInput == "2") and counter == 2):
    #     message.body("Please give us a location. Type the Street Name. For example 'Main Street'")
    #     counter = counter + 1
    #
    #     #response for rat evidence: "what type of evidence?"
    #     print (dict_evidence[userInput])
    #
    #     #print (counter)
    #     #print (currCase)
    #
    # # ------------ CASE 2, ERROR ----------------------------------------------
    # elif (counter == 2):
    #     message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
    #
    #     #reset counters to case 0
    #     userInput = 0
    #     counter = 0
    #     currCase = 0
    #
    #
    # # ----------------- CASE 1, rat sighting: location -------------------
    # if (userInput == "1" and counter == 1):
    #     message.body("Where did you see the rat? \n 1. Inside \n 2.Outside \n Type '1' or '2'")
    #     counter = counter + 1
    #     currCase = 1
    #
    #     #print (userInput)
    #     #print (counter)
    #     #print (currCase)
    #
    #
    # # ---------------- CASE 2, rat evidence: type of evidence -------------
    # elif (userInput == "2" and counter == 1):
    #     message.body("Please categorize your evidence:\n 1.Rat Droppings\n 2.Chewed boxes or food \n Type '1' or '2'")
    #     counter = counter + 1
    #     currCase = 2
    #
    #     #print (userInput)
    #     #print (counter)
    #     #print (currCase)
    #
    #
    # # -------------- CASE 3, rat prevention ------------------------------
    # elif (userInput == "3" and counter == 1):
    #     message.body("Thank you for your interest in rat prevention. Please follow this link for more info: linkhere")
    #     counter = 0
    #     currCase = 0
    #
    #     #print (userInput)
    #     #print (counter)
    #     #print (currCase)
    #
    #
    # # ---------- ERROR ---------------------------
    # elif(counter == 1):
    #     message.body("Sorry looks like there was an error. Please enter only the numbers provided as an option.\n Type 'RAT' to return to the main menu!")
    #
    #     #reset to case 0
    #     userInput = 0
    #     counter = 0
    #     currCase = 0




    response.append(message)
    return str(response)



if __name__ == "__main__":
    app.run(debug=True)
