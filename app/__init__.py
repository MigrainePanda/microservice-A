from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
    app.config['MYSQL_USER'] = 'cs361_samsmi'
    app.config['MYSQL_PASSWORD'] = '4423'
    app.config['MYSQL_DB'] = 'cs361_samsmi'
    app.config['MYSQL_CURSORCLASS'] = "DictCursor"
    
    return app

