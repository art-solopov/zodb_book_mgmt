from bottle import Bottle

from .templating import render
from db import db_middleware

from .authors import app as authors_app

base_app = Bottle()

@base_app.route('/')
def home():
    return render('home.html')

base_app.mount('authors', authors_app)

base_app = db_middleware(base_app)
