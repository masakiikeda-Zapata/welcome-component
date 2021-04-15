"""
This function saves a welcome message.
"""

import json

def concatenate(message, name):
    with open(message, "r") as f:
        input_message = json.load(f)
    with open(name, "r") as f:
        input_name = json.load(f)
    sentence = input_message["message"]+input_name["name"]

    message_dict = {}
    message_dict["sentence"] = sentence
    message_dict["schema"] = "sentence"

    with open("concatenate.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact