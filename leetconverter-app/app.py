import streamlit as st

from wordcloud import WordCloud

import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('Agg')

# Data

natophonetics = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu"}
leet_dict = {'a': '4','b': 'l3', 'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+', 'w': '\\/\\/', 'o': '0'}
leet_dict_gk = {'a': 'α', 'b': 'β', 'g': 'γ', 'd': 'δ', 'e': 'ε', 'z': 'ζ', 'h': 'η', 'th': 'θ', 'i': 'ι', 'k': 'κ', 'l': 'λ', 'm': 'μ', 'n': 'ν', 'x': 'ξ', 'o': 'ω', 'p': 'π', 'r': 'ρ', 't': 'τ', 'u': 'υ', 'ph': 'φ', 'ch': 'χ', 'ps': 'ψ', 's': 'σ'}


# Utils Functions

def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    fig = plt.figure(figsize=(20,10))
    plt.imshow(mywordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

def get_value(val, my_dict):
    for key ,value in my_dict.items():
        if val==key:
            return value

def get_natophonetics(term):
    result = ' '.join([natophonetics.get(i,i) for i in list(term.upper())])
    return result

def leet_converter(term):
    result = ' '.join([leet_dict.get(i,i) for i in list(term.lower())])
    return result

def greek_leet_converter(term):
    result = ' '.join([leet_dict_gk.get(i,i) for i in list(term.lower())])
    return result
