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

natophonetics = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu"}
leet_dict = {'a': '4','b': 'l3', 'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+', 'w': '\\/\\/', 'o': '0'}

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

def get_natophonetics(term):
    result = " ".join([natophonetics.get(i,i) for i in list(term.upper())])
    return result

def leet_converter(term):
    result = " ".join([leet_dict.get(i,i) for i in list(term.lower())])
    return result
    
