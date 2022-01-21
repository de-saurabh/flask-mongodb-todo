from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hello')
def hello_from_other_world():
    return 'Hello from mars!!!!'


@app.route('/return_hello/<name>')
def return_hello(name):
    return f'Hello {name}'




