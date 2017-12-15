
# The manager file __init__.py . This has been set to keep a track of all the files of the app


from flask import Flask

app = Flask(__name__)

from app import index,authors,setcookie,getcookie,cookie,request,ht,input