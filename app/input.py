#TASK 7 of HPDF
#We input in textbox at from.html present at '/input' and return data to '/output'

from flask import Flask, request, render_template

from app import app
@app.route('/input')
def inp():
    return render_template('from.html')

@app.route('/output', methods=['POST'])
def output():
    entered_text=request.form['text']
    print(entered_text)
    return 'You entered: {}'.format(entered_text)