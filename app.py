from flask import Flask, request
from flask_cors import CORS
from flask_mysqldb import MySQL 

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs361_samsmi'
app.config['MYSQL_PASSWORD'] = '4423'
app.config['MYSQL_DB'] = 'cs361_samsmi'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def home_page():
    return "Microservice A for User Auth @ Endpoint '/auth'"

@app.route("/auth", methods=['POST'])
def auth():
    data = request.json
    email = data['email']
    password = data['password']
        
    cur = mysql.connect.cursor()
    query = f"SELECT password FROM Users WHERE email='{email}'"
    cur.execute(query)
    res = cur.fetchone()
       
    payload = {"auth_message": False}
    if res['password'] == password:
        payload = {"auth_message": True}
    return payload


if __name__ == '__main__':
    app.run(port=56329, debug=True)