#Task 1 of HPDF

# This displays a simple string "Hello World-Abhinav" on the browser on calling '/' or '/index'


from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World - Abhinav"