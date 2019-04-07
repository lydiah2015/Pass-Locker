


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
                print("Removed credential: %s"%(name))
                return 
        print("Credential:%s not found"%(name))


    