'''
REST API
Minimal API

Use APScheduler to call refresh 
'''

import atexit
import sched
from flask import Flask
from scraper import scraper
from flask_restful import Resource, Api, abort, reqparse
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
api = Api(app)

shced = BackgroundScheduler(daemon = True)
sched.add_job(scraper, 'interval', minutes = 60)
sched.start()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

# Shut down scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)