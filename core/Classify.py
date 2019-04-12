from . import Listen
from . import APIs
from . import DB
import sys
from . import SentimentAnalysis
from nltk.tokenize import sent_tokenize, word_tokenize

def classifyCommand(command):
    # Tokenize string of sentences into list of sentences
    commands = sent_tokenize(Listen.typeCommand(command))
    print(commands)
    #commands = Listen.typeCommand()
    #print(commands)
    questions, answers = processCommands(commands)
    # INSERT NEW QUESTiON in DB
    DB.insert_DB(questions, answers)

    for i in range(len(answers)):
        # print(questions[i]," : " ,answers[i])
        # print("")
        print("BOT:"+ str(answers[i]))
        return("BOT:"+ str(answers[i]))


def processCommands(commands):

    interogate_words = ['?', 'which', 'what', 'whose ', 'who', 'whom', 'where', 'when', 'how', 'why', 'whether']
    greeting_words = ['hello', 'hi', 'hey', 'good']
    self_words = ['you', 'your', 'yours']
    replies = []

    # for command in commands:
    #     command = command.lower()


    ## CHECK IN DATABASE
    # command = commands
    # print("command:",command)
    # Check if its personal

    for command in commands:
        db_return = DB.check_DB(command)
        if(db_return!=None):
            #return [command],[db_return]
            replies += [str(db_return) + "(FROM DATABASE)"]
        elif command=='x':
            sys.exit()

        elif any(word in command for word in self_words):

            #check if its personal + interogative
            if any(word in command for word in interogate_words):
                #replies += ["Asking personal Questions"]
                replies += [APIs.get_api_ai(command)]
            else:
                replies += [APIs.get_api_ai(command)]

        #check if its interogative
        elif any(word in command for word in interogate_words):
            #return APIs.wolf(command)
            replies += [APIs.wolf(command)]

        # check if its greetings
        elif any(word in command for word in greeting_words):
            #return APIs.get_api_ai(command)
            replies += [APIs.get_api_ai(command)]

        else:
            #return "Yet TO declare"
            try:
                print(questions[i]," : " ,answers[i])
            except:
                replies += [APIs.wolf(command) ]

    return commands,replies


if __name__ == "__main__":
    while(True):
        classifyCommand(command)




