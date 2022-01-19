from flask import Flask, request
import requests

# other
import re
import datetime

app = Flask(__name__)


@app.route("/image", methods=['POST'])
def image():
    if request.method == 'POST':
        request_data = request.get_json()
        user_id = request_data['userID']
        image_url = request_data['imageURL']
        time = re.sub(r"[,.:;@#?!&$]+\ *", "-", datetime.now())

        r = requests.get(image_url)
        with open(user_id + "-" + time + '.png', 'wb') as f:
            f.write(r.content)
        
        return "IMAGE RECIEVED BY USER " + user_id
    else:
        return '''
        ERROR: Requesting @ route /image with method other than POST.
            Only post method is supported. 
            Upon using post, the resulting image will be sent back.
        '''

if __name__ == '__main__':
   app.run(debug = True)