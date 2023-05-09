from flask import Flask
import flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello World from {flask.request.host_url}'

if __name__ == '__main__':
   app.run(host="0.0.0.0")