from gtts import gTTS
import speech_recognition as sr
from urllib.request import FancyURLopener
import pyttsx3
import requests
import threading

# Takes Type input
def typeCommand(command):
    #command = input("USER :")
    check = command.startswith('zero')
    if check:
        command1 = command.replace('zero',"")
        return command1
    else:
        return ""




def speak(s,audio):
    try:
        import pythoncom
        pythoncom.CoInitialize()
        print("Asistnt: "+audio)
    except:
        print("Asistnt: "+audio)



    try:
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate+0)
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

        engine.say(audio)
        #engine.connect('started-word', onWord)
        engine.runAndWait()
    except:
        engine.stop()
        try:
            engine.say(audio)
            #engine.connect('started-word', onWord)
            engine.runAndWait()
        except:
            engine.stop()

def talkToMe(audio):
    "speaks audio passed as argument"
    t = threading.Thread(target= speak, name="thread1", args= (0,audio))
    t.start()


# Takes Vice input
def voiceCommand():
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
        command = myCommand();
    except:
        print("No Internet connection bye")
        talkToMe("No Internet connection bye")
        sys.exit()
    return command






