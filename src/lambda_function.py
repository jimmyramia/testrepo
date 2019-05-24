'''
REST endpoint lambda code for displaying generic message or echoing a custom message
'''
import os
import json
import datetime

def lambda_handler(event, context):
    '''
    Lambda handles GET and POST requests for /
    '''
    if event['httpMethod'] == 'GET':
        return get()
    elif event['httpMethod'] == 'POST':
        body = ""
        try:
            body = json.loads(event['body'])
            print(body)
        except:
            return {'statusCode': 400, 'body': 'malformed json input'}
        return post(body)

def get():
    '''
    Returns generic message plus time
    '''
    today = datetime.datetime.today()
    return json.dumps({"message": 'Automation For The People', "timestamp": today.strftime('%m/%d/%Y:%H:%M:%S')})

def post(request_body):
    '''
    Echos the message you sent in the body of the request in the response
    '''
    today = datetime.datetime.today()
    if 'message' not in request_body:
        return {'statusCode': 400, 'body': 'missing message in request body'}
    return json.dumps({"message": request_body['message'], "timestamp": today.strftime('%m/%d/%Y:%H:%M:%S')})
