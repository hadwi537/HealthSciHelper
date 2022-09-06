import os
from urllib import request

from flask import Flask, render_template, request
from flask_mysqldb import MySQL


def create_app(test_config=None):
    '''
    This is the application factory
    Handles configuration, registration etc
    '''
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    
    # initaliase database connection with factory functions 
    with app.app_context():
        from . import db
        mysql = db.get_db()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/papers', methods = ['GET', 'POST'])
    def papers():
        # Displays database contents
        if request.method == 'GET':
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM papers")
            data = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()

            return render_template('database.html', data=data)
    
    return app