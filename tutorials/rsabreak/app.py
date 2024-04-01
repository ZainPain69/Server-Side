#!/usr/bin/python

from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
    return '<h1>Welcome to RSA Security</h1>' 

@app.route('/note')
def note():
    return render_template('note.html') 

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port='5000', ssl_context=('CERT.pem', 'priv_key.pem')) 
    app.run(host='0.0.0.0', port='5000')
    