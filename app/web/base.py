from bottle import Bottle

base_app = Bottle()

@base_app.route('/')
def home():
    return 'Hello, world!'
