from collections import namedtuple

import ZODB, ZODB.FileStorage
from BTrees.OOBTree import OOBTree

from ._base import models_registry as registry

DBInfo = namedtuple('DBInfo', ('storage', 'db', 'connection', 'root'))

def open_db():
    storage = ZODB.FileStorage.FileStorage('data.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    return DBInfo(storage, db, connection, root)

def db_middleware(app):
    def f(environ, start_response):
        info = open_db()
        environ['dbinfo'] = info
        response = app(environ, start_response)
        info.connection.close()
        info.db.close()
        return response
    return f
