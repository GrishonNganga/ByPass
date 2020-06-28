import sys
from users import User

def main():
    home = True
    while home:
        print(' -----------------------------------------------------------------------------------------------')
        print('|\t\t\t\t\t\t\t\t\t\t\t\t| \n|\t\t\t\tWELCOME\tTO\tBY-PASS\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|\n|\t\t\t*MANGE ALL YOUR PASSWORDS IN ONE PLACE*\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|\n|\tSelect a number to continue...\t\t\t\t\t\t\t\t|\n|1. Join BY-PASS\t\t\t\t\t\t\t\t\t\t|\n|2. Login to BY-PASS\t\t\t\t\t\t\t\t\t\t|\n|3. Exit BY-PASS\t\t\t\t\t\t\t\t\t\t|\n|\t\t\t\t\t\t\t\t\t\t\t\t|')
        print(' -----------------------------------------------------------------------------------------------')

        option = input()
        if option == '1':
            signup = False
            while not signup:
                print('--------------------------------------------------------')
                print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter first name\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                print('--------------------------------------------------------')
                first_name = input()
                if first_name == '1':
                    signup = not signup
                else: 
                    print('--------------------------------------------------------')
                    print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter last name\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                    print('--------------------------------------------------------')
                    last_name = input()
                    if last_name == '1':
                        signup = not signup
                    else:
                        print('--------------------------------------------------------')
                        print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter your email\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                        print('--------------------------------------------------------')
                        email = input()
                        if email == '1':
                            signup = not signup
                        else:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter a password\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                            print('--------------------------------------------------------')
                            password = input()
                            if password == '1':
                                signup = not signup
                            else:
                                user_created = User(first_name, last_name, email, password)
                                if user_created.create_account():
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tUser created successfully!\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    status = input()
                                    if status == '1':
                                        signup = not signup
                                    else:
                                        signup = not signup
                                else:
                                    print('--------------------------------------------------------')
                                    print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tSomething wrong happened\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                                    print('--------------------------------------------------------')
                                    status = input()
                                    if status == '1':
                                        signup = not signup
                                    else:
                                        signup = not signup

        if option =='2':
            login = False
            while not login:
                print('--------------------------------------------------------')
                print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter your email\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                print('--------------------------------------------------------')
                email = input()
                if email == '1':
                    login = not login
                else:
                    print('--------------------------------------------------------')
                    print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|Please enter your password\t\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tEnter\t\t1. Cancel\t\t|')
                    print('--------------------------------------------------------')
                    password = input()
                    if password == '1':
                        login = not login
                    else:
                        account_status = User.check_account_exist(email, password)
                        if account_status:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tWE ARE IN\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                            print('--------------------------------------------------------')
                            in_bitch = input()

                        else:
                            print('--------------------------------------------------------')
                            print('|\t\t\t\t\t\t\t|\n|\tWe are glad you are here.\t\t\t|\n|\t\t\t\t\t\t\t|\n|\t\tAccount does not exist. Please Sign Up\t\t|\n|\t\t\t\t\t\t\t|\n|\t\t\tEnter\t\t\t\t|')
                            print('--------------------------------------------------------')
                            error = input()
                            login = not login

        elif option == '3':
            home = not home


if __name__ == '__main__':
    main()