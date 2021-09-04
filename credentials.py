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