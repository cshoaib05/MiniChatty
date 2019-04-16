from flask import Flask, render_template,request,flash, url_for, request, session, redirect
import requests
import json
import calendar
from core import Classify


from gtts import gTTS
import speech_recognition as sr
from urllib.request import FancyURLopener
import pyttsx3
import requests
import threading




app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':

        if request.form['question'] != 'NULL':

            question = request.form['question']

            answer = Classify.classifyCommand(question)
            # print(question)

            replied_answer = {
                'user_question' : question,
                'question': answer
            }
            
            return render_template('index.html', replied_answer = replied_answer)
    else:

        return render_template('index.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')



# //background process happening without any refreshing
@app.route('/',methods=['GET','POST'])
@app.route('/background_process_test')
def background_process_test():
    # print("Hello")
    # return "nothing"
    print("voice command start")
    #"listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        #r.pause_threshold = 1
        print('Ready...')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit=10)

    try:
        command = r.recognize_google(audio).lower()
        #talkToMe('Tumne ye bola: ' + command)
        print('You Said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        #print('Your last command couldn\'t be heard')
        #talkToMe("missed your words")
        print("missed your words")
        command = background_process_test();
    except:
        print("No Internet connection bye")
        talkToMe("No Internet connection bye")
        sys.exit()
    return command





if __name__ == '__main__':
    app.run(debug=True)