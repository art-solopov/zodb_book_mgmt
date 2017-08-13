from bottle import Bottle

from .templating import render

base_app = Bottle()

@base_app.route('/')
def home():
    return render('home.html')
