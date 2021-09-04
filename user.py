class User:
  """
  User class
  Args:
  login_name: To sign into the application.(str)
  pin : To sign into the application.(str)
  """
  user_list = []

  def __init__(self, login_name, pin):
    self.login_name = login_name
    self.pin = pin

  def save_user(self):
    """
    this method appends new object to user_list
    """
    User.user_list.append(self)

  @classmethod
  def user_auth(cls,name,pin):
    """
    This method returns a boolean True if the username and pin inputted
    matches those of a user in the user_list
    """
    for user in cls.user_list:
      if user.login_name == name and user.pin == pin:
        return True
    
    return False