import unittest
from app import app

class Tests(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check for user


if __name__ == "__main__":
    unittest.main()
    
        