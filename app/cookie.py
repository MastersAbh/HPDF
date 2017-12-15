#This is where the app is redirected once the cookie has been set

from app import app
from flask import Flask

@app.route('/cookie')
def cookie():
    return "Your Cookie has been set!"