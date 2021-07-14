import unittest, sys

sys.path.append('../Webframe_project') # imports python file from parent directory
from flask_trial import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
				
    def test_home(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
				
    def test_second_page(self):
        response = self.app.get('/second_page', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
				
    def test_register(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
				
if __name__ == "__main__":
    unittest.main()
		