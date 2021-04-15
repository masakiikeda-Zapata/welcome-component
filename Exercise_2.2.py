"""
This function saves a welcome message.
"""

import json

def yourName(name):

    message_dict = {}
    message_dict["name"] = name
    message_dict["schema"] = "name"

    with open("yourName.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact