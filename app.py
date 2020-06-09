from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from DateTime import DateTime
from datetime  import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


db = SQLAlchemy(app)


a =0
pa = "the-password"
cap = 25
ad = "iRWOJRnHZDlIsCm63EbJfwkXJkhngbitJw=="
su = "4kr6XeFX3aZjvv1aCKKhWW4bvcPGULmgHA=="
re = "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="
en = "+saF6NWKEgyrqRt02gol/k2nagxeWhLQkA=="
ex = "RfZDtKHDFntlZz3MmAnIJPGtAdYIqhZQCw=="

peoplein  = "Jesus Christ,Dimitri Blaiddyd"

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(60))
	address = db.Column(db.String(100))
	people = db.Column(db.Integer)
	gone = db.Column(db.Integer)
	enter_time = db.Column(db.DateTime, default=datetime.now)
	leave_time = db.Column(db.DateTime)

class Party(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lname = db.Column(db.String(60))
	address = db.Column(db.String(100))


@app.route('/')
@app.route('/home')
def index():
	global a
	b = cap-a
	return render_template('index.html',c=a,ca=b, cap=cap)

@app.route('/admin')
def admin():
	global a
	b = cap-a
	return render_template('admin.html',)

@app.route('/see')
def  see():
	return str(a)

@app.route('/pass1', methods=["POST","GET"])
def passw1():
	bp =  ""
	request.get_data(as_text=True)
	b = request.data
	bp = str(b, 'utf-8')
	print("Administrator attempted login with: ",bp)
	if(bp == "the-password"):
		print("Admin logged in")
		return "U_R_IN"
	else:
		abort(403)

@app.route('/pass2', methods=["POST",  "GET"])
def passw2():
	bp = ""
	request.get_data(as_text=True)
	b = request.data
	bp = str(b, 'utf-8')
	print("Lifegaurd attempted login with: ", bp)
	if(bp == "a-password"):
		print("Admin logged in")
		return "U_R_GOOD"
	else:
		return "U_R_BAD"


@app.route('/pass2', methods=["POST", "GET"])
#used for debugging when activated(run 'python app.py' to debug)
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)