import atexit
from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from DateTime import DateTime
from datetime  import datetime
import os
from apscheduler.scheduler import Scheduler

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


db = SQLAlchemy(app)

cron = Scheduler(daemon=True)
cron.start()

day = datetime.now()

a =0
pa = "the-password"
pa2="a-password"
cap = 25
cp = "iRWOJRnHZDlIsCm63EbJfwkXJkhngbitJw=="
cn = "4kr6XeFX3aZjvv1aCKKhWW4bvcPGULmgHA=="
re = "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="
ca = "+saF6NWKEgyrqRt02gol/k2nagxeWhLQkA=="
de = "RfZDtKHDFntlZz3MmAnIJPGtAdYIqhZQCw=="
se = "/kh++rjC2D72yDeLIRDF375yJ6nQZaO/mQ=="
ad = "NNsXq7wEuLvrt0mG3b6KqdMx0/3ZwfVolw=="
su = "zAH2XnWb6HzhgngMGYYxaIpGI36L3LHyCQ=="

@cron.interval_schedule(hours=24)
def job_function():
	global day
	day = datetime.now()


class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lname = db.Column(db.String(60))
	address = db.Column(db.String(100))
	peopleat = db.Column(db.Integer)
	peoplemax = db.Column(db.Integer)
	enter_time = db.Column(db.DateTime)
	leave_time = db.Column(db.DateTime)

class Party(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lname = db.Column(db.String(60))
	address = db.Column(db.String(100))
	pay = db.Column(db.Integer, default=0)


@app.route('/')
@app.route('/home')
def index():
	A = datetime.now()
	B = datetime.today()
	print(A>B)
	print(B>A)
	print(day)
	global a
	b = cap-a
	return render_template('index.html',c=a,ca=b, cap=cap,se=se)

@app.route('/admin')
def admin():
	global a
	b = cap-a
	dude = Party.query.filter_by(pay=1).all()
	dedu = Party.query.filter_by(pay=0).all()
	return render_template('admin.html', dat=dude, det=dedu,cp=cp,cn=cn,re=re,ca=ca,de=de)

@app.route("/lifegaurd")
def life():
	b = cap-a
	return render_template('register.html', se=se, ad=ad, su=su,c=a,ca=b,cap=cap)

@app.route('/search', methods=["POST","GET"])
def search():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (se+pa2)):
			bo1 = bool(Party.query.filter_by(lname=b.get('lname'),pay=1).first())
			if(bo1):
				dude = Party.query.filter_by(lname=b.get('lname'),pay=1).all()
				table = '<table class="table table-bordered table-striped"><tr><th>id</th><th>Last Name</th><th>address</th><th>pay</th></tr>'
				for c in dude:
					table += ('<tr><td>'+str(c.id)+'</td><td>'+c.lname+'</td><td>'+c.address+'</td><td>'+str(c.pay)+'</td></tr>')
				table += '</table>'
				print(table)
				return table
			else:
				return "No"
		else:
			abort(403)
	else:
		abort(403)

@app.route('/add', methods=["POST", "GET"])
def add():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (ad+pa2)):
			global a
			bo1 = bool(Party.query.filter_by(lname=b.get('lname'), address=b.get("address"),pay=1).first())
			if(bo1):
				bo2 = bool(Person.query.filter(Person.lname==b.get('lname'), Person.address==b.get("address"), Person.peopleat >= 1).first())
				if(bo2):
					i = int(b.get("people"))
					person2 = Person.query.filter(Person.lname==b.get('lname'),Person.address==b.get('address'),Person.peopleat>=1).first()
					person2.peopleat += i
					if(person2.peopleat > person2.peoplemax):
						person2.peoplemax = person2.peopleat
					db.session.commit()
					print("It did it also")
					a += i
					return("It w2")
				else:
					i = int(b.get("people"))
					person1 = Person(lname=b.get('lname'), address=b.get('address'),peopleat=i,peoplemax=i,enter_time=datetime.now())
					db.session.add(person1)
					db.session.commit()
					print("It did it")
					a += i
					return("It w1")
			else:
				return("No")
		else:
			abort(403)
	else:
		abort(403)

@app.route('/sub', methods=["POST","GET"])
def sub():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (su+pa2)):
			global a
			bo1 = bool(Person.query.filter(Person.lname==b.get('lname'),Person.address==b.get('address'),Person.peopleat >= 1).first())
			if(bo1):
				i = int(b.get("people"))
				person = Person.query.filter(Person.lname==b.get('lname'),Person.address==b.get("address"),Person.peopleat >= 1).first()
				if(i <= person.peopleat):
					person.peopleat -= i
					if(person.peopleat == 0):
						person.leave_time = datetime.now()
					db.session.commit()
					a -= i
					return("It w")
				else:
					return ("tm")
			else:
				return("No")
		else:
			abort(403)
	else:
		abort(403)

@app.route('/see')
def  see():
	return str(a)

@app.route('/register', methods=["POST", "GET"])
def reg():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (re+pa)):
			bo = bool(Party.query.filter_by(lname=b.get('lname'),address=b.get('address')).first())
			if(bo == False):
				i = int(b.get('pay'))
				party = Party(lname=b.get('lname'), address=b.get('address'),pay=i)
				db.session.add(party)
				db.session.commit()
				print("it did it")
				return ("It worked")
			else:
				return "No"
		else:
			abort(403)
	else:
		abort(403)

@app.route('/cpay', methods=["POST", "GET"])
def cpay():
	if(request.is_json):
		b =  request.get_json()
		print(b)
		if(b.get('key') ==  (cp+pa)):
			bo = bool(Party.query.filter_by(lname=b.get('lname'),address=b.get('address')).first())
			if(bo):
				i = int(b.get('pay'))
				print(i)
				party = Party.query.filter_by(lname=b.get('lname'), address=b.get('address')).first()
				party.pay = i
				print("It did it")
				db.session.commit()
				return ("It worked")
			else:
				print("NO")
				return ("No")
		else:
			abort(403)
	else:
		abort(403)

@app.route('/caddress', methods=["POST","GET"])
def caddress():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key')  ==  (ca+pa)):
			bo = bool(Party.query.filter_by(lname=b.get('lname'),address=b.get('address')).first())
			if(bo):
				party = Party.query.filter_by(lname=b.get('lname'), address=b.get("address")).first()
				party.address = b.get("naddress")
				print("It did it")
				print(party.address)
				db.session.commit()
				return("It worked")
			else:
				print("NO")
				return ("No")
		else:
			abort(403)
	else:
		abort(403)

@app.route('/clname', methods=["POST", "GET"])
def clname():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (cn+pa)):
			bo = bool(Party.query.filter_by(lname=b.get('lname'),address=b.get('address')).first())
			if(bo):
				party = Party.query.filter_by(lname=b.get('lname'), address=b.get('address')).first()
				party.lname = b.get("nlname")
				print("It did it")
				db.session.commit()
				return ("It worked")
			else:
				print("NO")
				return ("No")
		else:
			abort(403)

	else:
		abort(403)

@app.route('/delt', methods=["POST", "GET"])
def delt():
	if(request.is_json):
		b = request.get_json()
		print(b)
		if(b.get('key') == (de+pa)):
			bo = bool(Party.query.filter_by(lname=b.get('lname'),address=b.get('address')).first())
			if(bo):
				Party.query.filter_by(lname=b.get('lname'), address=b.get('address')).delete()
				db.session.commit()
				print("It did  it")
				return("It worked")
			else:
				print("No")
				return("No")
		else:
			abort(403)
	else:
		abort(403)

@app.route('/pass1', methods=["POST","GET"])
def passw1():
	bp =  ""
	request.get_data(as_text=True)
	b = request.data
	bp = str(b, 'utf-8')
	print("Administrator attempted login with: ",bp)
	if(bp == pa):
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
	if(bp == pa2):
		print("Admin logged in")
		return "U_R_GOOD"
	else:
		return "U_R_BAD"

#used for debugging when activated(run 'python app.py' to debug)
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)