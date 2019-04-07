


class Credential:

    def __init__(self):
        self.credentials_list=[]

    def add_credential(self,name,login,password):
        cred={
            "name":name,
            "login":login,
            "password":password
        }
        self.credentials_list.append(cred)

    def remove_credential(self,name):
        for cred in self.credentials_list:
            if cred["name"]==name:
                self.credentials_list.remove(cred)
                return True
        print("Credential:{} not found".format(name))
        return False

    