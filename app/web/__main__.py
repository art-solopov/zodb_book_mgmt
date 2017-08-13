import bottle
from .base import base_app
bottle.run(app=base_app, host='localhost', port='8080', debug=True)
