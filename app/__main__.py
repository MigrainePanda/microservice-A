from flask import request
from flask_mysqldb import MySQL 
from app import create_app

app = create_app()
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
    app.run(debug=True)