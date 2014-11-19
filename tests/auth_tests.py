__author__ = 'Vivan'


import unittest

from uberipy.uber import Uber
from uberipy.errors import UberipyException


class UberipyAuthTests(unittest.TestCase):

    def setUp(self):
        self.mock_server_token = ''
        self.mock_client_id = 'TbP2woYDfL2_pPuBxM2r-Q8OoPr6BFBwKUtXw4s1'
        self.mock_secret = 'UcAhCFC2SdKXKb26_7Njwmyy8LtuSg552C5ZQ9yCvB'

    def test_server_token_empty(self):
        """ Testing for a case where server token is empty """
        self.assertRaises(UberipyException, Uber, self.mock_client_id, self.mock_server_token, self.mock_secret)

    def test_server_token_not_present(self):
        """ Testing for a case when server token is not present when instantiating """
        self.assertRaises(UberipyException, Uber, self.mock_client_id, None, self.mock_secret)

if __name__ == '__main__':
    unittest.main()
