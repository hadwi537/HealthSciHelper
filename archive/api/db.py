'''
connect to the database

g is a special key unique for every request
Stores data that might be accessed by multiple functions during the request
'''
from flask import current_app, g
from flask_mysqldb import MySQL
import click

# eventually want something like this

def get_db():
    '''
    Establish connection to file
    '''
    if 'db' not in g:
        db_host   = '192.168.2.14'
        db_name   = 'fvision'
        db_user   = 'webuser'
        db_passwd = 'insecure_db_pw'
        current_app.config['MYSQL_HOST'] = db_host
        current_app.config['MYSQL_USER'] = db_user
        current_app.config["MYSQL_PASSWORD"] = db_passwd
        current_app.config["MYSQL_DB"] = db_name

        g.db = MySQL(current_app)
    return g.db