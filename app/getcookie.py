#TASK 4 of HPDF
#Here it Fetches the set cookie with http://localhost:5000/getcookies and displays the stored key-values in it.


from app import app
from flask import Flask,request, jsonify

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    s={}
    s['name']=name
    s['age']=age
    return jsonify(Cookies=s)
