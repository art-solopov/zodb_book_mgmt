import persistent.list as plist
from BTrees.OOBTree import OOBTree

from ._base import Base

class IdExistError(Exception):
    pass

class Book(Base):
    def __init__(self, authors=None, publisher=None, year=None, title=''):
        self.authors = plist.PersistentList(authors or [])
        self.publisher = publisher
        self.year = year
        self.title = title
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if self._id is None:
            self._id = value
        else:
            raise IdExistError()


class Author(Base):
    def __init__(self, name=''):
        self.name = name
        self.books = OOBTree()


class Publisher(Base):
    def __init__(self, name=''):
        self.name = name
        self.books = OOBTree()
