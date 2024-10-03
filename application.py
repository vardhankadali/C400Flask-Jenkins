# a simple hello world program using Flask in one file

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello WORELD!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# plssssssss
