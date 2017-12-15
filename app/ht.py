#TASK 6 of HPDF
#We render an HTML page web.html and display it

from app import app
from flask import Flask,render_template

@app.route('/html')

def view():
    return render_template('web.html')