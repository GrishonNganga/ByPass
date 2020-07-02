import csv, os, random
class Credential:
    database = 'credentials.csv'
    def __init__(self, email, account, password):
        self.email = email
        self.account = account
        self.password = password

    def get_email(self):
        return self.email
    
    def get_account(self):
        return self.account

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
    
    def create_credential(self):
        file_exist = os.path.isfile(Credential.database)
        with open(Credential.database, 'a')as file_to_write:
            if not file_exist:
                fields = ['email', 'account', 'password']
                file_data = csv.DictWriter(file_to_write, fieldnames=fields, lineterminator='\n')
                file_data.writeheader()
                file_data.writerow({
                    'email': self.get_email(),
                    'account': self.get_account(),
                    'password': self.get_password() 
                })
                return True
            else:
                fields = ['email', 'account', 'password']
                file_data = csv.DictWriter(file_to_write, fieldnames=fields, lineterminator='\n')
                file_data.writerow({
                    'email': self.get_email(),
                    'account': self.get_account(),
                    'password': self.get_password() 
                })
                return True

    def check_account_exist(self):
        with open(Credential.database, 'r')as read_file:
            fields = ['email', 'account', 'password']
            read_data = csv.DictReader(read_file, fieldnames=fields)
            for line in read_data:
                if line['email'] == self.get_email() and line['account'] == self.get_account():
                   return True
            return False

    @classmethod
    def check_an_account_exist(cls, email, account):
        db_present = os.path.isfile(Credential.database)
        if db_present:
            with open(Credential.database, 'r')as read_file:
                fields = ['email', 'account', 'password']
                file_data = csv.DictReader(read_file, fieldnames=fields)
                for line in file_data:
                    if line['email'] == email and line['account'] == account:
                        return True
                return False
        else: return False
   
    @classmethod
    def randomizer(cls):
        password = ''
        alphabets = "ab(cdefg^hi%jklm+no#pqrs@tuv)wxyz!*_"
        special ='!^%@(*)#_+@'
        for i in range(8):
            random_number = random.randrange(1, 26)
            password += alphabets[random_number]
        return password

    @classmethod
    def display_accounts(cls, email):
        file_exist = os.path.isfile(Credential.database)
        all_user_accounts = []
        if file_exist:
            with open(Credential.database, 'r')as accounts_file:
                all_accounts = csv.DictReader(accounts_file)
                for account in all_accounts:
                    if account['email'] == email:
                        all_user_accounts.append(account)
                return all_user_accounts
        else:
            return all_user_accounts

    def delete_account(cls, email, account):
        db_exists = os.path.isfile(Credential.database)
        if db_exists:
            accounts_non_delete = []
            with open(Credential.database, 'r')as cred_file:
                cred_data = csv.DictReader(cred_file)
                for account in cred_data:
                    if account['email'] == email and account['account'] != account:
                        accounts_non_delete.append(account)
            
            with open(Credential.database, 'w')as cred_file_write:
                fields = ['email', 'account', 'password']
                non_delete_accounts = csv.DictWriter(cred_file_write, fieldnames=fields, lineterminator='\n')
                non_delete_accounts.writeheader()
                for account in accounts_non_delete:
                    writerow(account)

                return True
        
        return False