from flask import Flask
from flask import jsonify
from flask import request

import argparse
import json

app = Flask('COCA Wallpaper App')

@app.route('/configure', methods=['GET'])
# get user preferences: ROUGH LAYOUT YOU CAN CHANGE :)
#   1. Use weather for wallpaper generator? Use news? Toggle music? What they want?
#   1a. Are we getting Evan to make music? cause it would be sick but also depends on evan
#
#   2a. If weather, find location to configure to
#   2b. If news, uhhh idk
#
#   3a. Check if all information is gettable
#   3b. If gettable then send request, otherwise send back error msg
def configure():
    return


@app.route('/wallpaper', methods=['POST'])
# put out the wallpapers
# I think maybe we can just send get requests to DALL-E API and post those
def sendWallpapers():
    return