#TASK 3 of HPDF

#Sets a simple cookie at http://localhost:5000/setcookie with the following values: name=Abhinav and age=20 and then redirects to '/cookie' confirming the work


from app import app
from flask import jsonify, Flask, make_response,redirect

@app.route('/setcookie')
def setCookie():
    resp = make_response(redirect('/cookie'))
    resp.set_cookie('name', 'Abhinav')
    resp.set_cookie('age','20')
    return resp