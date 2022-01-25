from ntpath import join
from flask import Flask, request
import requests
import os

# other
import re
import datetime

app = Flask(__name__)

@app.route("/")
def root():
    return 'Welcome from yoga260!'

@app.route("/hi")
def hello():
    return 'Hi from yoga260!'


@app.route("/bye")
def bye():
    return "Bye from yoga260!"

@app.route("/ls")
def ls():
    return "  |  ".join(os.listdir("."))

@app.route("/image", methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        request_data = request.get_json()
        user_id = request_data['userID']
        image_url = request_data['imageURL']
        # time = re.sub(r"[,.:;@#?!&$]+\ *", "-", datetime.now())
        # r = requests.get(image_url)
        # with open(user_id + "-" + time + '.png', 'wb') as f:
        #     f.write(r.content)
        
        return '''REQUEST RECIEVED
        >> UserId: {}
        >> imageUrl: {}'''.format(user_id, image_url)
    else:
        return '''
        ERROR: Requesting @ route /image with method other than POST.
            Only post method is supported. 
            Upon using post, the resulting image will be sent back.
        '''

@app.route("/pwd")
def get_pwd():
    return os.getcwd()

if __name__ == '__main__':
   app.run(debug = True)