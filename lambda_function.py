import os
import json
import boto3
import datetime

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        return get()
    elif event['httpMethod'] == 'POST':
        body = ""
        try:
            body = json.loads(event['body'])
        except:
            return {'statusCode': 400, 'body': 'malformed json input'}
        if 'message' not in body:
            return {'statusCode': 400, 'body': 'missing message in request body'}
        return post(body)

def get():
    today = datetime.datetime.today()
    return {'body': json.dumps({"message": 'Automation For The People', "timestamp": today.strftime('%m/%d/%Y:%H:%M:%S')})}

def post(body):
    today = datetime.datetime.today()
    return {'body': json.dumps({"message": body['message'], "timestamp": today.strftime('%m/%d/%Y:%H:%M:%S')})}
