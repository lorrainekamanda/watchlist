import unittest

from model import User,Role,Comment

class UserTest(unittest.TestCase):

    def setUp(self):

        self.new_user = User(password='leilanjeri')

    def test__passoword_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch= Role(role_id=1,role_title='Insiprational',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",user = self.user_James )


