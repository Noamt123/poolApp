from flask import Flask
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

a =0
pa = "the-password"

@app.route('/')
@app.route('/home')
def index():
	global a
	return render_template('index.html',c=a)

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
	b = 25-a
	return render_template('admin.html', c=a, p=pa, ca=b)


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
	b = request.data
	b3 = str(b, 'utf-8')
	if(br == "CuRUkhogic7YvKv0ak6oAJaH1g7uY8z2gA=="):
		a = 0
		print(str(a))
		return (str(a))
	else:
		abort(403)

@app.route('/see')
def  see():
	return ("there are ", str(a), " people in the pool.\n", str(25-a), " more people can enter the pool\n\n", "The pool's capacity is 25")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)