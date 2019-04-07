import string
import random
from user import User

def print_message_head(message):
    print("*"*50)
    print(message.upper())
    print("*"*50+"\n")

def login():
    username=input("Username: ")
    password= input("Password: ")
    user.username=username
    user.password=password


def select_option():
    print("\nChose an option:\n")
    print("1)Add existing account.\n2)Add new account.\n3)Delete credential.\n4)List Credentials.\n5)Exit.")
    option=int(input("Option: "))
    return option


# option 1
def add_existing_account():
    name=input("Account name:")
    login=input("Login: ")
    password=input("Password: ")
    user.credential.add_credential(name,login,password)
    input("Done, Press Enter to Continue")


# option 2 
def add_new_account():
    name=input("Account name:")
    login=input("Login: ")
    print("\nChose an option:\n")
    print("1)Set password.\n2)Generate password.\n")
    option=int(input("Option: "))
    if option == 1:
        password=input("Password: ")
    elif option == 2:
        pass_length=int(input("Password Length: "))
        password="".join(random.choices(string.ascii_letters+string.digits,k=pass_length))
    else:
        print("Invalid option!!")
        return 
    user.credential.add_credential(name,login,password)
    input("Done, Press Enter to Continue")
 

def list_credentials():
    print("#"*50)
    for cred in user.credential.credentials_list:
        print(
            "Account Name: %s    Login: %s    Password: %s"%(cred["name"],cred["login"],cred["password"])
        )
    print("#"*50)
    input("Done, Press Enter to Continue")

if __name__=="__main__":
    print_message_head("Welcome To Password Locker")
    # create new User
    user=User("","")
    # login user to set username & password
    login()

    while True:
        option=select_option()
        if option ==1:
            add_existing_account()

        if option == 2:
            add_new_account()

        if option == 4:
            list_credentials()

        if option == 5:
            print("Bye!!")
            break
