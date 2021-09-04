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