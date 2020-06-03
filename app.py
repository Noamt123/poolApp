from flask import Flask
from flask import render_template
app = Flask(__name__)
a = 0
@app.route('/')
def index():
	print(a)
	return render_template('index.html', thing=a)

@app.context_processor
def context_processor():
	return dict(poop=0)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)