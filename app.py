from flask import Flask
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

a =0
pa = "the-password"
cap = 25
ad = "iRWOJRnHZDlIsCm63EbJfwkXJkhngbitJw=="
su = "4kr6XeFX3aZjvv1aCKKhWW4bvcPGULmgHA=="
re = "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="

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

#used for debugging when activated(run 'python app.py' to debug)
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)