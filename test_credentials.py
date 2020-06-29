import unittest
from credentials import Credential
from users import User
import csv, os

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.test_user_credential = Credential('grishon.nganga01@gmail.com', 'Twitter', '123@Iiht')
        self.test_other_user_credential = Credential('grishon.nganga01@gmail.com', 'Instagram', '123@Iiht')

    def tearDown(self):
        if os.path.isfile(Credential.database):
            os.remove(Credential.database)
    
    def test_intialize_credential(self):
        '''Function that tests if Credential class is created successfully.'''

        self.assertEqual('grishon.nganga01@gmail.com', self.test_user_credential.get_email())
        self.assertEqual('Twitter', self.test_user_credential.get_account())
        self.assertEqual('123@Iiht', self.test_user_credential.get_password())


    def test_create_credentials_file(self):
        
        with open(Credential.database, 'w+') as test_file:
            file_exists = os.path.isfile(Credential.database)
            self.assertTrue(file_exists)

    def test_record_a_credential(self):
        self.test_user_credential.create_credential()
        self.test_other_user_credential.create_credential()
        with open(Credential.database, 'r')as read_file:
            fields = ['email', 'account', 'password']
            data_read = csv.DictReader(read_file, fields, lineterminator='\n')
            self.add_success = False
            counter = 0
            for line in data_read:
                counter += 1
                if line['email'] == 'grishon.nganga01@gmail.com' and line['account'] == 'Twitter' and line['password'] == '123@Iiht':
                    self.add_success = True 
   
            self.assertTrue(self.add_success)

    def test_check_account_exist(self):
        self.test_user_credential.create_credential()

        account_exist = self.test_user_credential.check_account_exist()
        self.assertTrue(account_exist)

    def test_check_account_exist(self):
        self.test_user_credential.create_credential()

        account_exist = Credential.check_an_account_exist(self.test_user_credential.get_email(), self.test_user_credential.get_account())
        self.assertTrue(account_exist)

    def test_check_account_exist_without_db(self):
        account_exist = Credential.check_an_account_exist(self.test_user_credential.get_email(), self.test_user_credential.get_account())
        self.assertFalse(account_exist)

    def test_randomizer(self):
        random_password = Credential.randomizer()
        self.assertGreater(len(random_password), 7)
        self.assertLess(len(random_password), 9)

if __name__ == '__main__':
    unittest.main()