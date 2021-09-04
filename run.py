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

def check_existing_credential(platform):
  """
  Function that check if a credential exists with that number and return a Boolean
  """
  return Credential.credential_exists(platform)


def display_credentials():
  """
  Function that returns all the saved credentials
  """
  return Credential.display_credentials()


def copy_password(platform):
  """
  Function which copies the password of the platform
  taken as an argument
  """
  return Credential.copy_password(platform)


def generate_password(length):
  """
  Function which generates a random password
  Args:
    the desired password length
  """
  return Credential.generate_password(length)

def main():
    cprint("""
                        ____________
                      .~      ,   . ~.
                     /                \
                    /      /~\/~\   ,  \
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@

 $$\    $$\  $$$$$$\  $$\   $$\ $$\    $$$$$$$$\ 
$$ |   $$ |$$  __$$\ $$ |  $$ |$$ |   \__$$  __|
$$ |   $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |   
\$$\  $$  |$$$$$$$$ |$$ |  $$ |$$ |      $$ |   
 \$$\$$  / $$  __$$ |$$ |  $$ |$$ |      $$ |   
  \$$$  /  $$ |  $$ |$$ |  $$ |$$ |      $$ |   
   \$  /   $$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |   
    \_/    \__|  \__| \______/ \________|\__|   
    GREETINGS USER, WELCOME TO THE PASSWORD VAULT                                         
                
        ""","blue")
    while True:
        cprint("""
        Use the following short codes to manage your account 
            'lg' - Login 
            'xx' - Close app
            ""","blue")
        print("What would you like to do?")
        code = input().lower()
        if code == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                login_name = input("Enter your username: ")
                login_pin = getpass("Enter your pin: ")
                print("Loading ...")
                time.sleep(1.5)
                print("\n")
                cprint("CONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED","green",attrs=['bold'])
                print("Sign into your new account")
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                save_user(create_user(login_name,login_pin))
                if authenticate_user(sign_in_name,sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    cprint("SUCCESSFULLY SIGNED IN","green",attrs=['bold'])  
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    # cprint("Oops, you entered the wrong username/pin, we have to do this again :(","red")
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                if authenticate_user(sign_in_name,sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    cprint("SUCCESSFULLY SIGNED IN","green",attrs=['bold'])  
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    # cprint("Oops, you entered the wrong username/pin, we have to do this again :(","red")
                    print("\n")
            while True:
                if authenticate_user(sign_in_name,sign_in_pin):
                    ####
                    cprint(
                        """
    O===[====================-
        
    WELCOME TO YOUR VAULT:
    Use the following commands to navigate the application:
        'cc' - enables you to create an a credential
        'dc' - displays the credentials you have saved
        'cp' - copies the password of a given credential
        'fc' - helps you find a credential by its platform name
        'dl' - deletes a credential
        'ex' - logs you out
        'help' - helps a user around the app
                        ""","blue")
                    print(f"At your service {sign_in_name}, what task would you like to perform?")
                    key_word = input().lower()

                    if key_word == 'cc':
                        print("Save a new credential")
                        platform = input("Input the platform: ")
                        print("\n")
                        username = input("Input your username: ")
                        print("\n")
                        email = input("Input your email: ")
                        print("\n")
                        option = input("Would you wish to have Vault generate a password for you? Y or N ").lower()
                        if option.startswith("y"):
                            print()
                            desired_len = int(input("How long would you like your password to be? Provide number only. "))
                            password = generate_password(desired_len)
                        else:
                            print("\n")
                            password = getpass("Enter your password: ")

                        save_credential(create_credential(platform,username,email,password))
                        print('\n')
                        cprint(f"NEW CREDENTIALS FOR {platform} CREATED!","green",attrs=['bold'])
                        print("_"*50)
                        print('\n')

                    elif key_word == 'dc':

                        if display_credentials():
                            print("HERE ARE YOUR CREDENTIALS")
                            print('\n')

                            for cred in display_credentials():
                                cprint(
                                    f"""
    --------------------------------------------------
            Platform --- {cred.platform}               
            Username --- {cred.username}               
            Email    --- {cred.email}                  
            Password --- {cred.password}               
    --------------------------------------------------
                                ""","magenta"
                                )
                                print('\n')
                        else:
                            print('\n')
                            cprint("You dont seem to have any credentials saved yet","yellow")
                            print("_"*50)
                            print('\n')

                    elif key_word == 'fc':
                        print("Enter the platform you want to search for")
                        print("\n")
                        platform_search = input()
                        if check_existing_credential(platform_search):
                            search_credential = find_credentials(platform_search)
                            cprint(
                                f"""
    -------------------------------------------------------
        Platform --- {search_credential.platform}               
        Username --- {search_credential.username}               
        Email    --- {search_credential.email}                  
        Password --- {search_credential.password}               
    -------------------------------------------------------
                                ""","magenta")
                            print("_"*50)
                        else:
                            cprint("The credential does not exist", "red")
                    
                    elif key_word == "cp":
                        print("Enter the platform whose password you would like copied")
                        platform_find = input()
                        print("Loading...")
                        if check_existing_credential(platform_find):
                            search_credential = find_credentials(platform_find)
                            pyperclip.copy(search_credential.password)
                            time.sleep(1.5)
                            print("\n")
                            cprint(f"PASSWORD FOR {search_credential.platform} HAS BEEN COPIED","green",attrs=['bold'])
                            print("_"*50)

                        else:
                            cprint("The platform you entered does not exist","yellow")
                            print("_"*50)
                    
                    elif key_word == "dl":
                        print("Enter the platform whose credentials you'd like to delete")
                        platform_delete = input()
                        if check_existing_credential(platform_delete):
                            print("Please wait ...")
                            platform_creds = find_credentials(platform_delete)
                            delete_credential(platform_creds)
                            time.sleep(1.5)
                            cprint(f"CREDENTIALS FOR {platform_creds.platform} SUCCESSFULY DELETED","green",attrs=['bold'])
                        else:
                            cprint("The credential does not exist", "red")

                    elif key_word == "ex":
                        print(f"Have a nice day {login_name}")
                        print("_"*50)
                        break

                    elif key_word == "help":
                        cprint(
                        """                       
    SORRY TO HERE YOU'RE STUCK
    PLEASE REFER TO WHAT IS BELOW
            .--.                   .---.
        .---|__|           .-.     |~~~|
        .--|===|--|_          |_|     |~~~|--.
        |  |===|  |'\     .---!~|  .--|   |--|
        |%%|   |  |.'\    |===| |--|%%|   |  |
        |%%|   |  |\.'\   |   | |__|  |   |  |
        |  |   |  | \  \  |===| |==|  |   |  |
        |  |   |__|  \.'\ |   |_|__|  |~~~|__|
        |  |===|--|   \.'\|===|~|--|%%|~~~|--|
        ^--^---'--^    `-'`---^-^--^--^---'--'
                        ""","blue")

                    else:
                        cprint("You entered an unknown keyword. Please use the provided keywords. Type '-help' if you're stuck","yellow")
                        print("_"*50)

                else:
                    cprint("Oops, you entered the wrong username/pin, we have to do this again :(","red",attrs=['bold'])
                    print("\n")
                    break
            
        elif code == "xx":
            cprint(
            """
        88                                                      
           88                                                      
           88                                                      
 ,adPPYba, 88,dPPYba,   ,adPPYba,  ,adPPYba, 8b,dPPYba, ,adPPYba,  
a8"     "" 88P'    "8a a8P_____88 a8P_____88 88P'   "Y8 I8[    ""  
8b         88       88 8PP""""""" 8PP""""""" 88          `"Y8ba,   
"8a,   ,aa 88       88 "8b,   ,aa "8b,   ,aa 88         aa    ]8I  
 `"Ybbd8"' 88       88  `"Ybbd8"'  `"Ybbd8"' 88         `"YbbdP"'  
                                                                      
            ""","blue")
            break

        else:
            cprint("You entered an unknown short code, please try again","yellow")
        
if __name__ == '__main__':
    main()