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
	gone = db.Column(db.Integer)
	enter_time = db.Column(db.DateTime, default=datetime.now)
	leave_time = db.Column(db.DateTime)

@app.route('/')
@app.route('/home')
def index():
	global a
	b = cap-a
	return render_template('index.html',c=a,ca=b, cap=cap)

@app.route('/add', methods=["POST", "GET"])
def add():
	b1 = ""
	global a
	request.get_data(as_text = True)
	b = request.data
	b1 = str(b, 'utf-8')
	if(b1 == "iRWOJRnHZDlIsCm63EbJfwkXJkhngbitJw=="):
		a += 1
		print(str(a))
		return (str(a))
	else:
		abort(403)

@app.route('/admin')
def admin():
	global a
	b = cap-a
	return render_template('admin.html', c=a, p=pa, ca=b, cap=cap, ad=ad, su=su, re=re)


@app.route('/sub',methods=["POST","GET"])
def sub():
	b2 = ""
	global a
	request.get_data(as_text=True)
	b = request.data
	b2 = str(b, 'utf-8')
	if(b2  == "4kr6XeFX3aZjvv1aCKKhWW4bvcPGULmgHA=="):
		a -= 1
		print(str(a))
		return (str(a))
	else:
		abort(403)

@app.route('/reset',methods=["POST", "GET"])
def reset():
	b3 = ""
	global a
	request.get_data(as_text=True)
	b = request.data
	b3 = str(b, 'utf-8')
	if(b3 == "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="):
		a = 0
		print(str(a))
		return (str(a))
	else:
		abort(403)

@app.route('/see')
def  see():
	return str(a)

@app.route('/pass', methods=["POST","GET"])
def passw():
	bp =  ""
	request.get_data(as_text=True)
	b = request.data
	bp = str(b, 'utf-8')
	print("attempted login with: ",bp)
	if(bp == "the-password"):
		print("Someone logged in")
		return "U_R_IN"
	else:
		return "U_R_WRONG"

@app.route('/checkin')
def checkin():
	b = cap-a

	return render_template('checkin.html',c=a,ca=b, cap=cap,peo=peoplein, en=en)

@app.route('/checkout')
def checkout():
	return render_template('checkout.html',ex=ex,peo=peoplein)

@app.route('/enter/<fname>', methods=["POST","GET"])
def enter(fname):
	bp = ""
	request.get_data(as_text=True)
	b = request.data
	bp =str(b, 'utf-8')
	bo = bool(Person.query.filter_by(fname=fname,gone=0).first())
	if(bp == "+saF6NWKEgyrqRt02gol/k2nagxeWhLQkA==" and bo ==  False):
		person = Person(fname=fname, gone=0)
		db.session.add(person)
		print(fname, " arrived at the pool")
		db.session.commit()
		return "It work"

	elif(bp == "+saF6NWKEgyrqRt02gol/k2nagxeWhLQkA==" and bo):
		return "Already here"
	else:
		return "No"

@app.route('/exit/<fname>', methods=["POST","GET"])
def exit(fname):
	bp = ""
	request.get_data(as_text=True)
	b = request.data
	bp = str(b, 'utf-8')
	bo = bool(Person.query.filter_by(fname=fname,gone=0).first())
	print(bo)
	if(bp == "RfZDtKHDFntlZz3MmAnIJPGtAdYIqhZQCw==" and bo):
		person = Person.query.filter_by(fname=fname, gone=0).first()
		person.gone = 1
		person.leave_time = datetime.now()
		print(fname, " left the pool")
		db.session.commit()
		return("It work")

	elif(bp == "RfZDtKHDFntlZz3MmAnIJPGtAdYIqhZQCw==" and bo == False):
		return "Gone"

	else:
		return "No"

#used for debugging when activated(run 'python app.py' to debug)
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)