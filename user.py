from credential import Credential

class User:
    """
    class that holds user details
    """ 
    user_list = [] 

    def __init__(self,username,password):

        """
        class that generates new intances of users
        """
        self.username = username
        self.password = password
        self.credential=Credential()
        
    def save_user(self):
        """
        method to save user's details
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        deletes user details from the array that has been saved
        """
        User.user_list.remove(self)