import unittest
from credential import Credential
 
class TestCredential(unittest.TestCase):
    def setUp(self):
        """
        run before each test
        """
        self.credential= Credential()

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            pass

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.credential.credentials_list,[])
    
    def test_add_new_credential(self):
        """
        test to test whether new credential added has been saved 
        """
        self.credential.add_credential("facebook","user@mail.com","password")
        self.assertEqual(len(self.credential.credentials_list),1)

    

if __name__ == '__main__':
    unittest.main()