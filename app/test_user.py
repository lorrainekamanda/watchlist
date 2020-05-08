import unittest

from model import User,Role,Comment

class UserTest(unittest.TestCase):

    def setUp(self):

        self.new_user = User(password='leilanjeri')

    def test__passoword_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def setUp(self):
        self.user_lorraine = User(username = 'lorraine',password = 'lorra', email = 'lorra@.gmailom')
        self.new_pitch= Role(role_id=1,role_title='Insiprational',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",user = self.user_James )
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.role_id,1)
        self.assertEquals(self.new_review.role_title,'Inspirational')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_lorraine)

