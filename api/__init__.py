import os

from flask import Flask
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
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # 
    db_host   = '192.168.2.14'
    db_name   = 'fvision'
    db_user   = 'webuser'
    db_passwd = 'insecure_db_pw'
    app.config['MYSQL_HOST'] = db_host
    app.config['MYSQL_USER'] = db_user
    app.config["MYSQL_PASSWORD"] = db_passwd
    app.config["MYSQL_DB"] = db_name

    mysql = MySQL(app)

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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/papers', methods = ['POST'])
    def papers():
        # Allows querying of the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM papers")
        cursor.close()
    

    return app