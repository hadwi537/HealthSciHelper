'''
connect to the database

g is a special key unique for every request
Stores data that might be accessed by multiple functions during the request
'''
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g


# eventually want something like this

def get_db():
    '''
    Establish connection to file
    '''
    if 'db' not in g:
       g.db = SQLAlchemy(current_app)

    return g.db


def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()
