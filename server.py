from flask import Flask, render_template,request,flash, url_for, request, session, redirect
import requests
import json
import calendar
from core import Classify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':

        if request.form['question'] != 'NULL':

            question = request.form['question']

            answer = Classify.classifyCommand(question)
            # print(question)

            replied_answer = {
                'question': answer
            }
            
            return render_template('index.html', replied_answer = replied_answer)
    else:
        return render_template('index.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)