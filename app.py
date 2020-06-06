from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from DateTime import DateTime
from datetime  import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

a =0
pa = "the-password"
cap = 25
ad = "iRWOJRnHZDlIsCm63EbJfwkXJkhngbitJw=="
su = "4kr6XeFX3aZjvv1aCKKhWW4bvcPGULmgHA=="
re = "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="

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

@app.route('/enter/<fname>', methods=["POST","GET"])
def enter(fname):
	person = Person(fname=fname, gone=0)
	db.session.add(person)
	db.session.commit()

	return "<h1>a person entered the pool</h1>"

@app.route('/exit/<fname>', methods=["POST","GET"])
def exit(fname):
	person = Person.query.filter_by(fname=fname, gone=0).first()
	person.gone = 1
	person.leave_time = datetime.now()
	db.session.commit()

	return '<h1>a person has left the pool</h1>'

#used for debugging when activated(run 'python app.py' to debug)
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)