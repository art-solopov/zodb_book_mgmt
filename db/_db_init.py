import ZODB, ZODB.FileStorage
from BTrees.OOBTree import OOBTree

from ._base import models_registry as registry

storage = ZODB.FileStorage.FileStorage('data.fs')
db = ZODB.DB(storage)

def ensure_index(index_name, transaction=None):
    if transaction:
        root = transaction.root
        if not hasattr(root, index_name):
            setattr(root, index_name, OOBTree())
        return getattr(root, index_name)
    else:
        with db.transaction() as conn:
            return ensure_index(index_name, conn)
