from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='zodb_book_mgmt',
    version='0.0a1.dev1',
    url='https://github.com/art-solopov/zodb_book_mgmt',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['ZODB', 'Flask'],
    extras_require={
        'dev': ['ipython', 'jedi']
    }
)
