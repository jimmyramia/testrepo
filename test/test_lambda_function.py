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
        Test get request
        '''
        response = lambda_function.get()
        message = response['message']
        self.assertEqual(message, 'Automation For The People')

    def test_lambda_post(self):
        '''
        Test post request passing a message that will just get echoed in the response
        '''
        test_message = 'this is a test'
        request = construct_post_request(test_message)
        response = lambda_function.post(request)
        message = response['message']
        self.assertEqual(message, test_message)

    def test_lambda_post_no_message(self):
        '''
        Test post request passing no message and ensure that the response is a 400 error
        '''
        request = construct_bad_post_request()
        response = lambda_function.post(request)
        self.assertEqual(response['statusCode'], 400)

if __name__ == '__main__':
    unittest.main()
