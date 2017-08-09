import persistent.list as plist

from ._base import Base

class Book(Base):
    def __init__(self, authors=None, publisher=None, year=None, title=''):
        self.authors = plist.PersistentList(authors or [])
        self.publisher = publisher
        self.year = year
        self.title = title


class Author(Base):
    def __init__(self, name=''):
        self.name = name


class Publisher(Base):
    def __init__(self, name=''):
        self.name = name
