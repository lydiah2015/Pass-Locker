
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


def add_existing_account():
    name=input("Account name:")
    login=input("Login: ")
    password=input("Password: ")
    user.credential.add_credential(name,login,password)
    

def list_credentials():
    print("#"*50)
    for cred in user.credential.credentials_list:
        print(
            "Account Name: %s    Login: %s    Password: %s"%(cred["name"],cred["login"],cred["password"])
        )
    print("#"*50)

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

        if option == 4:
            list_credentials()

        if option == 5:
            break
