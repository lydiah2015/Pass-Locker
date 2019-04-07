import unittest

from user import User
 

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        run before each test
        """
        self.new_user = User("icy","123456")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''


        self.assertEqual(self.new_user.username,"icy")
        self.assertEqual(self.new_user.password,"123456")
    
    def test_save_user(self):
        """
        test to test whether data of user added has been saved 
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        checks if we can save multiple user 
        '''
        self.new_user.save_user()
        test_user = User("diplo","654321") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test of whether saved user details can be deleted from  the array that has been saved
        """
        self.new_user.save_user()
        new_user2 = User("diplo","654321") #new user
        new_user2.save_user()
        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)
    

if __name__ == '__main__':
    unittest.main()