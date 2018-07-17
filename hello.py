from flask import Flask

app = Flask(__name__)

@ap.route('/')
def hello():
    return 'hello, World!'