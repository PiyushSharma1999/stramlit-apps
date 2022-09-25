import streamlit as st
import string 
import random

## characters to generate password from
all_characters_pattern = list(string.ascii_letters+string.digits+"!@#$%^&*()")
alphanumeric_patter = list(string.ascii_letters+string.digits)
common_passwd_pattern = ["password","computer","1234"]

def generate_random_password(characters,password_length=6):
    # shuffling the characters
    random.shuffle(characters)
    # picking random characters from the lis
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    # shuffling the resultant passeord
    random.shuffle(password)

    ### converting the list to string
    ### printing the list
    return ("".join(password))

def generate_random_password2(characters:list,password_length=6)->str:
    random.shuffle(characters)
    password = [random.choice(characters) for i in range(password_length)]
    result = "".join(password)
    return result