from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/user", methods=['GET', 'POST'])
def post():
	if(request.method =='GET'):
		return render_template('index.html')

	elif(request.method == 'POST'):
		value = request.form['input']
		return render_template('welcome.html', name=value)

if __name__ == "__main__":
	app.run()