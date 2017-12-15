#TASK 5 of HPDF

#We deny the request made to '/robots.txt' and redirect the user to error page 'http://httpbin.org/deny'


from app import app
from flask import Flask,make_response,redirect

@app.route('/robots.txt')

def request():
    resp = make_response(redirect('http://httpbin.org/deny'))
    return resp