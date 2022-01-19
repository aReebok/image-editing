# IMAGE_LINK = 'https://media.discordapp.net/attachments/860750045472358450/933063826419638352/20201031_110739.jpg?width=193&height=407'
# r = requests.get(IMAGE_LINK)

# with open('google_logo.png', 'wb') as f:
#     f.write(r.content)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Goodbye, World!</p>"


if __name__ == '__main__':
   app.run(debug = True)