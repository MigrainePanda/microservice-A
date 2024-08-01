from flask_mysqldb import MySQL 
from app import create_app

app = create_app()
mysql = MySQL(app)

@app.route("/", methods=['GET'])
def home_page():
    return "<p>hello world</p>"

@app.route("/auth", methods=['GET'])
def auth():
    cur = mysql.connect.cursor()
    query = "SELECT * FROM tablename"
    res = cur.execute(query)
    print(res)
    return "fklasjflkasjfls"

if __name__ == '__main__':
    app.run(debug=True)