import unittest

from model import User

class UserTest(unittest.TestCase):

    def setUp(self):

        self.new_user = User(password='leilanjeri')

    def test__passoword_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

