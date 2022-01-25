from ntpath import join
from flask import Flask, jsonify, request, send_from_directory
import requests
import os

# other
import re
from datetime import datetime

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
        return return_file

    elif request.method == 'GET':
        return "Use a post request to post an image to put through mosaic."
    else: 
        return "Use GET or POST only."

@app.route("/image/<path:path>")
def get_image(path):
    """Download the processed file"""
    return send_from_directory(os.getcwd(), path, as_attachment=True)

if __name__ == '__main__':
   app.run(debug = True)