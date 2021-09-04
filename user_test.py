import unittest
from user import User

class UserTest(unittest.TestCase):
  """
  Test class that defines test cases for the contact class behaviours.
  Args:
    unittest.TestCase: Inherits the testCase class that helps in creating test cases
  """
  def setUp(self):
    """
    Set up method to run before each test cases.
    """
    self.new_user = User("user100", "1100")
    
  def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_user.login_name, "user100")
    self.assertEqual(self.new_user.pin, "1100")

  def test_save_user(self):
    """
    test_save_user test case to test if the user object is saved into
    the user list
    """
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)

  def test_user_auth(self):
    """
    test_user_auth tests case to authenticate the user
    """
    self.assertTrue(self.new_user.user_auth("user100","1100"))

if __name__ == "__main__":
    unittest.main()