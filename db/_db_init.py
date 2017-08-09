import ZODB, ZODB.FileStorage
from BTrees.OOBTree import OOBTree

from ._base import models_registry

storage = ZODB.FileStorage.FileStorage('data.fs')
db = ZODB.DB(storage)

def db_init():
    with db.transaction() as conn:
        root = conn.root
        for model in registry:
            if not hasattr(root, model.model_name):
                setattr(root, model.model_name, OOBTree())
