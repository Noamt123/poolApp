from flask import Flask
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

a =0

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
	if(b1 == "MEGAJESUS"):
		a += 1
		print(str(a))
		return render_template('index.html')
	else:
		abort(403)

@app.route('/admin')
def admin():
	global a
	return render_template('admin.html', c=a)


@app.route('/sub',methods=["POST","GET"])
def sub():
	b2 = ""
	global a
	request.get_data(as_text=True)
	b = request.data
	b2 = str(b, 'utf-8')
	if(b2  == "MEGASATAN"):
		a -= 1
		print(str(a))
		return (str(a))
	else:
		abort(403)

@app.route('/pass', methods=["POST", "GET"])
def pass():
	p  = ""
	b = request.data
	p = str(b, 'utf-8')
	if(p == "J2iK+D35pUrgU+UzHcR+dN6qoiQ="):
		return "the-password"
	else:
		abort(403)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)