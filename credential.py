import pyperclip
import string
import random

class Credential:
    """
    a contact class
   
    __init__ method that helps us define properties for our objects.

    Args:
    platform: New credential platform name.(str)
    username : New username.(str)
    email: New credential email adress.(str)
    password : New credential password.(str)
    """
    #class variable; accessible within the entire class
    credential_list = []

    def __init__(self,platform,username,email,password):
        #self represents the instance of the variable
        self.platform = platform
        self.username = username
        self.email = email
        self.password = password
    
    def save_credential(self):
        """
        this method appends new object to credential_list
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        this method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)
    
    @classmethod
    def find_by_platform(cls,platform):
        '''
        Method that takes in a platform and returns a credential that matches that name.

        Args:
            platform: Name to search for
        Returns :
            Credential that matches the platform.
        '''

        for credential in cls.credential_list:
            if credential.platform == platform:
                return credential
    
    @classmethod
    def credential_exists(cls,platform):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            platform: Name to search if it exists in credential list
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credential in cls.credential_list:
            if credential.platform == platform:
                return True
            
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_password(cls,platform):
        """
        method that copies the credential password on the system clipboard
        """
        credential_found = Credential.find_by_platform(platform)
        pyperclip.copy(credential_found.password)

    @classmethod
    def generate_password(cls,length):
        """
        this method uses the string method to generate a password of random digits and letters
        the length of the password is determined by the length passed in the function's parameter 
        Args:
            the desired password length
        """
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return "".join(random.choice(chars) for i in range(length))