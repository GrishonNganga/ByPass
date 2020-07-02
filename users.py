import csv, os
class User:
    database = 'users.csv'
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
       
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    def account_created(self):
        with open(User.database, 'r') as check_creation:
            csv_data = csv.DictReader(check_creation)
            for line in csv_data:
                if line['email'] == self.get_email():   
                    return True
            return False

    def create_account(self):
        fields = ['first_name', 'last_name', 'email', 'password']
        file_exists = os.path.isfile(User.database)
        if not file_exists:
            with open(User.database, 'a') as new_users:
                csv_writer = csv.DictWriter(new_users, fieldnames=fields, lineterminator='\n')
                csv_writer.writeheader()
                csv_writer.writerow({
                    'first_name': self.get_first_name(),
                    'last_name': self.get_last_name(),
                    'email': self.get_email(),
                    'password': self.get_password()
                    })

                return True
        else:
            if self.account_created() == False:
                with open(User.database, 'a')as user:
                    csv_add_user = csv.DictWriter(user, fieldnames=fields, lineterminator='\n')
                    csv_add_user.writerow({
                    'first_name': self.get_first_name(),
                    'last_name': self.get_last_name(),
                    'email': self.get_email(),
                    'password': self.get_password()
                    })
                    return True
            else:
                return False        
        
    def delete_account(self):
        with open(User.database, 'r') as file:
            csv_file = csv.DictReader(file)

            holder = []
            counter_before = 0
            counter_after = 0
            for line in csv_file:
                counter_before += 1

                if line['email'] != self.get_email():
                    holder.append(line)

        with open(User.database, 'w')as to_write:
            fields = ['first_name', 'last_name', 'email', 'password']
            csv_writer = csv.DictWriter(to_write, fieldnames=fields, lineterminator='\n')
            csv_writer.writeheader()
            
            for hold in holder:
                csv_writer.writerow(hold)


    def read_file(self):
        try: 
            with open(User.database, 'r') as opened_file:    
                return opened_file.read()
        except FileNotFoundError:
            return None


    @classmethod
    def check_account_exist(self, email, password):
        with open(User.database, 'r') as check_creation:
            csv_data = csv.DictReader(check_creation)
            for line in csv_data:
                if line['email'] == email and line['password'] == password :   
                    return True
            return False

