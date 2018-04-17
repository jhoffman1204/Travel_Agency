from flask import Flask, render_template
from sqlalchemy import *
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from app import routes


app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'jhoffman1204'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cse305group'
app.config['MYSQL_DATABASE_DB'] = 'codedash'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

@app.route("/" , methods = ['GET' , 'POST'])
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()