class Credential:
    '''
    Credential class, stores users credentials
    '''
    def __init__(self):
        '''
        initialize user creds to empty list
        '''
        self.credentials_list=[]

    def add_credential(self,name,login,password):
        '''
        adds new creds to the list self.credentials_list as a dict
        '''
        cred={
            "name":name,
            "login":login,
            "password":password
        }
        self.credentials_list.append(cred)

    def remove_credential(self,name):
        '''
        deletes user credential by account name
        '''
        for cred in self.credentials_list:
            if cred["name"]==name:
                self.credentials_list.remove(cred)
                print("Removed credential: %s"%(name))
                return 
        print("Credential:%s not found"%(name))


    