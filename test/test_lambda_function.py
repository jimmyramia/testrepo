'''
Tests the functions in the lambda_function module
'''
import unittest
import src
from src import lambda_function
import json

def construct_post_request(message):
    '''
    Construct the body of a valid post request for testing
    '''
    data = {}
    data['message'] = message
    return data

def construct_bad_post_request():
    '''
    Construct the body with no message for testing
    '''
    data = {}
    return data

class MyTestCase(unittest.TestCase):
    def test_lambda_get(self):
        '''
        Test get request returns the text we expect
        '''
        response = lambda_function.get()
        message = json.loads(response['body'])['message']
        self.assertEqual(message, 'Automation For The People')

    def test_lambda_post(self):
        '''
        Test that response of post request contains message we pass in our request
        '''
        test_message = 'this is a test'
        request = construct_post_request(test_message)
        response = lambda_function.post(request)
        message = json.loads(response['body'])['message']
        self.assertEqual(message, test_message)

    def test_lambda_post_no_message(self):
        '''
        Test post request passing no message and verify that the response is a 400 error
        '''
        request = construct_bad_post_request()
        response = lambda_function.post(request)
        self.assertEqual(response['statusCode'], 400)

if __name__ == '__main__':
    unittest.main()
