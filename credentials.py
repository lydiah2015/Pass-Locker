class User:
    """
    class that holds user details
    """ 
    user_list = [] 

    def __init__(self,first_name,last_name,username,password):

        """
        class that generates new intances of contacts
        """

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        
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

class Credentials:

    def __init__(self):
        self.credentials_lists=[]]
