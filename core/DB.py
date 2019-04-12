import re
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
import difflib

connection = sqlite3.connect('chatbot.sqlite', check_same_thread=False)
cursor = connection.cursor()

# create the tables needed by the program
try:
    # create the table containing the words
    cursor.execute('CREATE TABLE IF NOT EXISTS chatHistory (id INTEGER PRIMARY KEY AUTOINCREMENT,question TEXT UNIQUE, answer TEXT UNIQUE)')
    # create the table containing the sentences
    # create association between weighted words and the next sentence
    #cursor.execute('CREATE TABLE associations (word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)')
except:
    pass

def check_DB(command):


    cursor.execute("SELECT question,id FROM chatHistory ORDER BY id")
    question_rows = cursor.fetchall()
    cursor.execute("SELECT answer,id FROM chatHistory ORDER BY id")
    answer_rows = cursor.fetchall()
    
    #print(question_rows, answer_rows)
    
    for i,row in enumerate(question_rows):
        for each_row in row:
            sequence = difflib.SequenceMatcher(isjunk=None,a=str(each_row),b=command)
            differnce = sequence.ratio()*100
            difference = round(differnce,1)
            #print(difference)
            if(difference>=85):
                return answer_rows[i]
                #return "Yes"

    
def insert_DB(H,B):
    for i in range(len(H)):
        try:
            cursor.execute('INSERT INTO chatHistory(question,answer) VALUES(?, ?)', (str(H[i]),str(B[i])))
        except:
            pass
    connection.commit()
    return
    
