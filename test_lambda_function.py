import unittest
import lambda_function
import json

class MyTestCase(unittest.TestCase):
    def test_lambda_get(self):
        response = lambda_function.get()
        json_string = json.dumps(response)
        body = json.loads(json_string)['body']
        message = json.loads(body)['message']
        self.assertEqual(message, 'Automation For The People')


if __name__ == '__main__':
    unittest.main()
