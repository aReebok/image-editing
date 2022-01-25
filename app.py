from ntpath import join
from flask import Flask, jsonify, request, send_from_directory
import requests
import os

# other
import re
from datetime import datetime

from pythonmosaic import *

app = Flask(__name__)

@app.route("/")
def root():
    return 'Welcome to Python Mosaic API for images and videos! Hosted on Heroku by aReebok.'

@app.route("/pwd")
def get_pwd():
    return os.getcwd()

@app.route("/ls")
def ls():
    return jsonify(os.listdir("."))

@app.route("/image", methods=['GET', 'POST', 'DELETE'])
def image():
    if request.method == 'POST':
        request_data = request.get_json()
        user_id = request_data['userID']
        image_url = request_data['imageURL']
        input_image = requests.get(image_url) 

        return_file = (user_id + "_" + re.sub(r"[,.:;@#?!&$]+\ *", "-", str(datetime.now())) + '.png').replace(' ', '-')
        with open(return_file, 'wb') as f:
            f.write(input_image.content)

        mosaic(return_file, return_file, 1)
        return return_file

    elif request.method == 'GET':
        return "Use a post request to post an image to put through mosaic."

    # elif request.method == 'DELETE':
    #     request_data = request.get_json()
    #     image = request_data['image']
    #     if os.path.exists(image):
    #         os.remove("")
    #         return "200 image " + image + " deleted "
    #     else: 
    #         return "404 image does not exist"
    else: 
        return "Use GET, POST, or DELETE only."

@app.route("/image/<path:path>")
def get_image(path):
    """Download the processed file"""
    return send_from_directory(os.getcwd(), path, as_attachment=True)

@app.route("/image/<path:path>", methods=['GET','DELETE'])
def del_image(path):
    if os.path.exists(path):
        os.remove(path)
        return 200
    else: 
        return 404


if __name__ == '__main__':
   app.run(debug = True)