"""
This function saves a welcome message.
"""

import json

def concatenate(message,name):

    sentence = message["message"]+name["name"]

    message_dict = {}
    message_dict["sentence"] = sentence
    message_dict["schema"] = "sentence"

    with open("concatenate.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact