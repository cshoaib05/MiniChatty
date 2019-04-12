import apiai
import os
import json
import wolframalpha
import wikipedia

client = wolframalpha.Client("4E3H79-A3ARKHYKU9")


TOKEN = '3b0e24b4a9754d8b977392a250774aaf'
CLIENT_ACCESS_TOKEN = os.environ.get('API_AI_TOKEN', TOKEN)
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request = ai.text_request()
request.session_id = os.environ.get('API_AI_SESSION_ID', 'dd60fde7-c6ab-4f38-9487-7300c42b4916')

    
def get_api_ai(command):
    try:
        request = ai.text_request()
        request.query = command
        response = request.getresponse().read()
        output = json.loads(response)
        answer = output["result"]["fulfillment"]["speech"]
        return answer
    except:
        try:
            res = client.query(command) 
            answer = next(res.results).text
            return answer            
        except:
            try:
                return wikipedia.summary(command)
            except:
                return "Nothing Found"

    
def wolf(command):
    try:
        res = client.query(command) 
        answer = next(res.results).text
        return answer
    except:
        try:
            request = ai.text_request()
            request.query = command
            response = request.getresponse().read()
            output = json.loads(response)
            answer = output["result"]["fulfillment"]["speech"]
            return answer
        except:
            try:
                return wikipedia.summary(command)
            except:
                return "Nothing Found"
