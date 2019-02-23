#!/bin/python

# Flask application for getting data and creating an API
#install flask using pip3 : pip3 install flask

from flask_bootstrap import Bootstrap
from flask import Flask ,render_template

app = Flask(__name__)

boostrap = Bootstrap(app)

# name by using  __my__grades = 46

#index home page
@app.route("/")
def index():
    return render_template('index.html')

#sign up page
@app.route('/SignUp')
def SignUp():
    return render_template('sign_up.html')

#sign in page
@app.route('/SignIn')
def SignIn():
    return render_template('sign_in.html')

#sign in page
@app.route('/Devices')
def Devices():
    return render_template('devices.html')

#sign in page
@app.route('/Settings')
def Settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run()

