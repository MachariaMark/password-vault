#!/usr/bin/env python3
import random
import pyperclip
import time
from termcolor import colored, cprint
from getpass import getpass
from credential import Credential
from user import User

def create_user(login_name, pin):
  """
  Function to create a new user
  """
  new_user = User(login_name,pin)
  return new_user

def save_user(user):
  """
  Function to save user details
  """
  user.save_user()

def authenticate_user(username,password):
  return User.user_auth(username,password)

def create_credential(platform,username,email,password):
  """
  Function to create a new credential
  """
  new_credential = Credential(platform,username,email,password)
  return new_credential

def save_credential(credential):
  """
  Function to save credential
  """
  credential.save_credential()


def delete_credential(credential):
  """
  Function to delete a credential
  """
  credential.delete_credential()


def find_credentials(platform):
  """
  Function that finds a credential by platform name and returns the credentials
  """
  return Credential.find_by_platform(platform)