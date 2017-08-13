from bottle import Bottle, request

from .templating import render

from app.domains.authors import GetAll

app = Bottle()

@app.route('/')
def index():
    get_all = GetAll(request.environ.get('dbinfo').root)
    objects = get_all()
    return render('authors/index.html', objects=objects)
