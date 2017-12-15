#Task 2 of HPDF.
#Here we use Json and Flask to communicate with each other by fetching JSON data from two different URL's and returning data which includes data from both URL's.

#Basically, here it:
#a. fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
#b. fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
#c. Respond with only a list of authors and the count of their posts (a newline for each author).


from app import app
from flask import jsonify, Flask
import urllib, json
import requests

@app.route('/authors')
def authors():
    f = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')
    authors = json.load(f)
    f.close()
    d={}
    for k in authors:
        d[k['id']]=k['name']
    g={}
    p = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
    posts = json.load(p)
    p.close()
    for k in posts:
        g[k['userId']]=0
    for k in posts:
        g[k['userId']]+=1
    s={}
    for k in authors:
        s[k['name']]=g[k['id']]
    return jsonify(Posts=s)