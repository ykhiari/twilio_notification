# imports
from scripts.twilionotifier import TwilioNotifier
import json
import argparse

# add an argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", required=True, help="Path to the input configuration file")
args = vars(parser.parse_args())

# load the conf file
with open(args["config"],"r") as jsonfile:
    conf = json.load(jsonfile)

# initialize a twilionotifier instance
tn = TwilioNotifier(conf)

# send a message to the rpi
tn.send("This message is sent from the raspberry pi.")