import unittest
import pyperclip
from credential import Credential

class TestCredential(unittest.TestCase):
  """
  Test class that defines test cases for the contact class behaviours.
  Args:
    unittest.TestCase: Inherits the testCase class that helps in creating test cases
  """
  def setUp(self):
    """
    Set up method to run before each test cases.
    """
    self.new_credential = Credential("Github", "user101", "user101@email", "QwerY23")

  def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_credential.platform, "Github")
    self.assertEqual(self.new_credential.username, "user101")
    self.assertEqual(self.new_credential.email, "user101@email")
    self.assertEqual(self.new_credential.password, "QwerY23")
    
  def test_save_credential(self):
    """
    test_save_credential test case to test if the credential object is saved into
    the credential list
    """
    self.new_credential.save_credential()  # saving the new contact
    self.assertEqual(len(Credential.credential_list), 1)

  def tearDown(self):
    """
    tearDown method that does clean up after each test case has run.
    """
    Credential.credential_list = []

  def test_save_multiple_contact(self):
    """
    test_save_multiple_credentials to check if we can save multiple credential
    objects to our credential list
    """
    self.new_credential.save_credential()
    test_credential = Credential("Bitbucket", "user2", "u@u.com", "123asdf")  # new contact
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list), 2)

  def test_delete_credential(self):
    """
    test_delete_credential to test if we can remove a credential from the credential list
    """
    self.new_credential.save_credential()
    test_credential = Credential("Bitbucket", "user2", "u@u.com", "123asdf")
    test_credential.save_credential()

    self.new_credential.delete_credential()  # Deleting a contact object
    self.assertEqual(len(Credential.credential_list), 1)
    
  def test_find_by_platform(self):
    """
    test to check if we can find a credential by platform name and display information
    """

    self.new_credential.save_credential()
    test_credential = Credential("Bitbucket", "user2", "u@u.com", "123asdf")
    test_credential.save_credential()

    found_credential = Credential.find_by_platform("Bitbucket")

    self.assertEqual(found_credential.platform, test_credential.platform)

  def test_credential_exists(self):
    """
    test to check if we can return a Boolean  if we cannot find the credential.
    """

    self.new_credential.save_credential()
    test_credential = Credential("Bitbucket", "user2", "u@u.com", "123asdf")
    test_credential.save_credential()

    self.assertTrue(Credential.credential_exists("Bitbucket"))
    
  def test_display_credentials(self):
    """
    method that returns a list of all saved credentials
    """
    self.assertEqual(Credential.display_credentials(), Credential.credential_list)
    
  def test_copy_password(self):
    """
    Test to confirm that we are copying the password from a found credential
    """

    self.new_credential.save_credential()
    Credential.copy_password("Github")

    self.assertEqual(self.new_credential.password,pyperclip.paste())

  def test_generate_password(self):
    """
    Test to confirm that the password we are generating ahs the desired length
    """
    self.new_credential.save_credential()
    generated_password = Credential.generate_password(12)
    test_credential = Credential("Bitbucket", "user2", "u@u.com", generated_password)
    test_credential.save_credential()

    self.assertEqual(len(test_credential.password),12)

if __name__ == "__main__":
    unittest.main()