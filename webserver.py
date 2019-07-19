# Imported Modules
from flask import Flask, render_template, redirect, url_for, request, flash, redirect, abort, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

# Application for webserver
app = Flask(__name__)
app.secret_key = 'dafkjdfoe9854a89tyudi'
db = SQLAlchemy(app)

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Weeke' or request.form['password'] != '1nzyij3sib59de8s':
            error = 'Login attempt failed! Your username or password is incorrect!'
        else:
            return redirect(url_for('home'))  
    return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/admin')
def home():
    return '''
    <!doctype html>
<html>
	<head>
		<title>Dashboard - Shell Backdoor</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	<body>
		<h1>Hello World!</h1>
	</body>
</html>
    '''

# Client information upload page
@app.route('/client')
def client():
    return 'Client information upload page'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')